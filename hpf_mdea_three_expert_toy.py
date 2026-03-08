import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle
from matplotlib.widgets import Slider


class HPFMDEAThreeExpertToy:
    """
    Smooth HPF–MDEA 3-expert visualization.

    Experts:
      GR    -> stable star regime
      QPRCA -> collapse / extreme compression regime
      QFT   -> ringdown / dissipation regime
    """

    def __init__(self):
        self.fig = plt.figure(figsize=(15, 8))

        self.ax_scene = self.fig.add_axes([0.05, 0.18, 0.58, 0.74])
        self.ax_info = self.fig.add_axes([0.67, 0.18, 0.30, 0.74])
        self.ax_slide = self.fig.add_axes([0.10, 0.07, 0.50, 0.05])

        self.slider = Slider(self.ax_slide, "Evolution", 0, 100, valinit=0, valstep=0.5)
        self.slider.on_changed(self.update)

        self.setup_axes()
        self.create_scene_artists()
        self.update_info_panel(0)
        self.update(0)

    def setup_axes(self):
        self.ax_scene.set_xlim(0, 10)
        self.ax_scene.set_ylim(0, 10)
        self.ax_scene.set_facecolor("#050714")
        self.ax_scene.set_aspect("equal")
        self.ax_scene.set_xticks([])
        self.ax_scene.set_yticks([])
        self.ax_scene.set_title("Star → Black Hole → Dissipation")

        self.ax_info.set_xlim(0, 1)
        self.ax_info.set_ylim(0, 1)
        self.ax_info.set_facecolor("#0d1020")
        self.ax_info.set_xticks([])
        self.ax_info.set_yticks([])
        self.ax_info.set_title("HPF / MDEA Domain Routing")

    def create_scene_artists(self):
        # Keep center fixed so nothing "jumps" sideways.
        self.cx, self.cy = 5.0, 5.0

        # Star glow layers
        self.star_glow_1 = Circle((self.cx, self.cy), 2.2, color="orange", alpha=0.0, lw=0)
        self.star_glow_2 = Circle((self.cx, self.cy), 1.8, color="orange", alpha=0.0, lw=0)
        self.star_glow_3 = Circle((self.cx, self.cy), 1.5, color="orange", alpha=0.0, lw=0)
        self.star_core = Circle((self.cx, self.cy), 1.2, color="#ffd84d", ec="#fff3a6", lw=2, alpha=0.0)

        self.ax_scene.add_patch(self.star_glow_1)
        self.ax_scene.add_patch(self.star_glow_2)
        self.ax_scene.add_patch(self.star_glow_3)
        self.ax_scene.add_patch(self.star_core)

        # Black hole layers
        self.bh_ring_1 = Circle((self.cx, self.cy), 1.45, fill=False, ec="#8ec3ff", lw=2, alpha=0.0)
        self.bh_ring_2 = Circle((self.cx, self.cy), 1.65, fill=False, ec="#507dd9", lw=1.5, alpha=0.0)
        self.bh_core = Circle((self.cx, self.cy), 0.85, color="black", ec="#d9e6ff", lw=1.4, alpha=0.0)

        self.ax_scene.add_patch(self.bh_ring_1)
        self.ax_scene.add_patch(self.bh_ring_2)
        self.ax_scene.add_patch(self.bh_core)

        # Ringdown waves
        self.wave_patches = []
        for i in range(6):
            c = Circle((self.cx, self.cy), 1.8 + i * 0.35, fill=False, ec="#b8d4ff", lw=1.5, alpha=0.0)
            self.wave_patches.append(c)
            self.ax_scene.add_patch(c)

    def clamp(self, x, lo=0.0, hi=1.0):
        return max(lo, min(hi, x))

    def smoothstep(self, x):
        x = self.clamp(x)
        return x * x * (3 - 2 * x)

    def lerp(self, a, b, t):
        return a + (b - a) * t

    def phase_weights(self, s):
        """
        Smooth regime blending:
          0–30   GR dominant
          30–65  QPRCA takeover
          65–100 QFT takeover
        """
        gr = 1.0 - self.smoothstep((s - 20) / 15.0)      # fades out by ~35
        qprca_in = self.smoothstep((s - 25) / 15.0)      # fades in around 25–40
        qprca_out = 1.0 - self.smoothstep((s - 65) / 12.0)  # fades out around 65–77
        qprca = qprca_in * qprca_out
        qft = self.smoothstep((s - 65) / 15.0)           # fades in around 65–80

        total = gr + qprca + qft
        if total <= 0:
            return 0.0, 0.0, 1.0
        return gr / total, qprca / total, qft / total

    def update_scene(self, s):
        gr_w, qprca_w, qft_w = self.phase_weights(s)

        # Collapse progress for radius changes
        collapse_t = self.smoothstep((s - 30) / 35.0)
        ring_t = self.smoothstep((s - 65) / 35.0)

        # Star shrinks smoothly and fades
        star_r = self.lerp(1.30, 0.45, collapse_t)
        self.star_core.set_radius(star_r)
        self.star_core.set_alpha(0.95 * gr_w + 0.25 * qprca_w)

        self.star_glow_1.set_radius(star_r * 1.8)
        self.star_glow_2.set_radius(star_r * 1.5)
        self.star_glow_3.set_radius(star_r * 1.3)

        self.star_glow_1.set_alpha(0.15 * gr_w)
        self.star_glow_2.set_alpha(0.12 * gr_w)
        self.star_glow_3.set_alpha(0.10 * gr_w)

        # Black hole grows in smoothly
        bh_core_r = self.lerp(0.35, 0.90, collapse_t)
        self.bh_core.set_radius(bh_core_r)
        self.bh_core.set_alpha(0.25 * qprca_w + 0.95 * qft_w + 0.75 * qprca_w)

        self.bh_ring_1.set_radius(bh_core_r * 1.6)
        self.bh_ring_2.set_radius(bh_core_r * 1.85)
        self.bh_ring_1.set_alpha(0.9 * (qprca_w + 0.5 * qft_w))
        self.bh_ring_2.set_alpha(0.7 * (qprca_w + 0.5 * qft_w))

        # Ringdown waves expand smoothly
        for i, wave in enumerate(self.wave_patches):
            base_r = 1.8 + i * 0.38
            wave.set_radius(base_r + ring_t * 1.8)
            alpha = max(0.0, 0.42 - i * 0.055) * qft_w * (1.0 - 0.35 * ring_t)
            wave.set_alpha(alpha)

    def clear_info(self):
        self.ax_info.cla()
        self.ax_info.set_xlim(0, 1)
        self.ax_info.set_ylim(0, 1)
        self.ax_info.set_facecolor("#0d1020")
        self.ax_info.set_xticks([])
        self.ax_info.set_yticks([])
        self.ax_info.set_title("HPF / MDEA Domain Routing")

    def status_bar(self, x, y, val, label):
        w = 0.65
        h = 0.025

        self.ax_info.text(x, y + h + 0.01, label, color="white", fontsize=9)
        self.ax_info.add_patch(Rectangle((x, y), w, h, fc="#12182f", ec="#7c8fb8", lw=1))

        color = "#55b6ff"
        if val > 0.45:
            color = "#ffc24d"
        if val > 0.78:
            color = "#ff6f6f"

        self.ax_info.add_patch(Rectangle((x, y), w * self.clamp(val), h, fc=color))

    def box(self, y, title, lines, active=False):
        x = 0.05
        w = 0.90
        h = 0.17

        fc = "#22365e" if active else "#171d33"
        ec = "#89b7ff" if active else "#55607e"

        self.ax_info.add_patch(
            FancyBboxPatch(
                (x, y), w, h,
                boxstyle="round,pad=0.02",
                fc=fc, ec=ec, lw=1.5
            )
        )

        self.ax_info.text(x + 0.02, y + h - 0.035, title, color="white", fontsize=11, weight="bold")

        yy = y + h - 0.075
        for line in lines:
            self.ax_info.text(x + 0.025, yy, line, color="#dbe6ff", fontsize=9)
            yy -= 0.045

    def update_info_panel(self, s):
        self.clear_info()

        gr_w, qprca_w, qft_w = self.phase_weights(s)

        # Smooth metrics
        entropy = 0.28 * gr_w + 0.86 * qprca_w + 0.60 * qft_w
        curvature = 0.25 * gr_w + 0.88 * qprca_w + 0.55 * qft_w
        bandwidth = 0.30 * gr_w + 0.79 * qprca_w + 0.50 * qft_w

        self.status_bar(0.08, 0.78, entropy, "Entropy")
        self.status_bar(0.08, 0.73, curvature, "Curvature")
        self.status_bar(0.08, 0.68, bandwidth, "Bandwidth")

        active = "GR"
        if qprca_w >= gr_w and qprca_w >= qft_w:
            active = "QPRCA"
        elif qft_w > gr_w and qft_w > qprca_w:
            active = "QFT"

        if active == "GR":
            obs = [
                "Low entropy and curvature",
                "Geometry safely inside GR domain",
                "No saturation limits reached"
            ]
            routing = [
                "Selected Expert: GR",
                "Action: maintain geometric evolution",
                "Reason: system inside GR scope"
            ]
            outcome = [
                "Stable star.",
                "No domain transition required."
            ]
        elif active == "QPRCA":
            obs = [
                "Entropy phase gate crossed",
                "Curvature exceeds GR safe scope",
                "Compression approaching substrate limits"
            ]
            routing = [
                "Outgoing Expert: GR",
                "Incoming Expert: QPRCA",
                "Action: reversible substrate update",
                "Constraint: finite bandwidth enforced"
            ]
            outcome = [
                "Star collapses toward black hole",
                "Illegal compression avoided"
            ]
        else:
            obs = [
                "Peak compression has passed",
                "Entropy and curvature falling",
                "System leaving substrate danger zone"
            ]
            routing = [
                "Outgoing Expert: QPRCA",
                "Incoming Expert: QFT",
                "Action: field-level dissipation handling",
                "Emission and relaxation regime"
            ]
            outcome = [
                "Black hole ringdown and dissipation",
                "Experts handed control cleanly"
            ]

        self.box(0.47, "HPF Observation", obs, True)
        self.box(0.27, "MDEA Routing Decision", routing, active != "GR")
        self.box(0.08, "Outcome", outcome)

        # Add blend readout so viewer sees the handoff continuously
        self.ax_info.text(
            0.08, 0.94,
            f"Blend  GR {gr_w:.2f}   QPRCA {qprca_w:.2f}   QFT {qft_w:.2f}",
            color="#dbe6ff", fontsize=10
        )

    def update(self, val):
        s = float(val)
        self.update_scene(s)
        self.update_info_panel(s)
        self.fig.canvas.draw_idle()

    def run(self):
        plt.show()


if __name__ == "__main__":
    toy = HPFMDEAThreeExpertToy()
    toy.run()
