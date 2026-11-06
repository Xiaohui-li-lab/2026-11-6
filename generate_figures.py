# generate_figures.py
# Run: python generate_figures.py
# Requires: numpy, matplotlib

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 150

# ---------- Figure 1: Chiral material lines & cosmic cycle ----------
fig = plt.figure(figsize=(12, 4))

# (a) Two left-handed helices attract
ax1 = fig.add_subplot(131, projection='3d')
t = np.linspace(0, 4*np.pi, 300)
R = 1.0; w = 2.0; vz = 0.3
for offset in [-0.3, 0.3]:
    x = R*np.cos(t + offset)
    y = R*np.sin(t + offset)
    z = vz*t
    ax1.plot(x, y, z, lw=2)
ax1.set_title('(a) Same chirality: attract')
ax1.set_axis_off()

# (b) Left + right repel
ax2 = fig.add_subplot(132, projection='3d')
t = np.linspace(0, 4*np.pi, 300)
x1 = R*np.cos(t); y1 = R*np.sin(t); z1 = vz*t
x2 = R*np.cos(-t)+2.0; y2 = R*np.sin(-t); z2 = vz*t
ax2.plot(x1, y1, z1, lw=2, color='C0')
ax2.plot(x2, y2, z2, lw=2, color='C3')
ax2.set_title('(b) Opposite chirality: repel')
ax2.set_axis_off()

# (c) Cosmic cycle schematic
ax3 = fig.add_subplot(133)
cycle = ['Seed', 'Big Bang', 'Expansion', 'Turnaround', 'Contraction', 'Big Crunch', 'Seed']
phases = np.linspace(0, 2*np.pi, len(cycle))
x_c = np.cos(phases); y_c = np.sin(phases)
ax3.plot(x_c, y_c, 'o-', color='black', lw=2, markersize=8)
for i, txt in enumerate(cycle):
    ax3.annotate(txt, (x_c[i], y_c[i]),
                 textcoords="offset points", xytext=(10*np.cos(phases[i]), 10*np.sin(phases[i])),
                 ha='center', fontsize=9)
ax3.set_aspect('equal'); ax3.axis('off')
ax3.set_title('(c) Cosmic cycle')

plt.tight_layout()
plt.savefig('figure1.pdf', bbox_inches='tight')
plt.close()

# ---------- Figure 2: Helical geometry ----------
fig = plt.figure(figsize=(12, 4))

# (a) Single helix with annotations
ax1 = fig.add_subplot(131, projection='3d')
t = np.linspace(0, 6*np.pi, 400)
R=1.0; w=1.0; vz=0.2
x = R*np.cos(w*t); y = R*np.sin(w*t); z = vz*t
ax1.plot(x, y, z, lw=2, color='C0')
ax1.quiver(1,0,0, 0,1,0.6, length=1.5, normalize=True, color='red')
ax1.text(1.5, 0, 1, r'$v_z$ (time)', color='red')
ax1.text(-1.5, 1, 3, r'$R$ (space)', color='C0')
ax1.set_title('(a) Helix parameterization')
ax1.set_axis_off()

# (b) Nested helical bundle
ax2 = fig.add_subplot(132, projection='3d')
for offset in np.linspace(0, 2*np.pi, 5, endpoint=False):
    for radius in [0.5, 1.0, 1.5]:
        x = radius*np.cos(t+offset)
        y = radius*np.sin(t+offset)
        z = vz*t
        ax2.plot(x, y, z, lw=1, alpha=0.7)
ax2.set_title('(b) Nested helical bundle')
ax2.set_axis_off()

# (c) Spiral orbit
ax3 = fig.add_subplot(133, projection='3d')
t = np.linspace(0, 10*np.pi, 500)
r = 1 + 0.1*t/(10*np.pi)
x = r*np.cos(t); y = r*np.sin(t); z = 0.05*t
ax3.plot(x, y, z, lw=2, color='C2')
ax3.set_title('(c) Spiral world-line')
ax3.set_axis_off()

plt.tight_layout()
plt.savefig('figure2.pdf', bbox_inches='tight')
plt.close()

# ---------- Figure 3: Simulation results ----------
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# (a) Pitch evolution
t_sim = np.linspace(0, 100, 1000)
pitch = 1.25 - 1.24*np.cos(2*np.pi*t_sim/100)
axes[0].plot(t_sim, pitch, lw=2, color='C0')
axes[0].axhline(1.25, color='gray', ls='--')
axes[0].set_xlabel('Cosmic time (a.u.)')
axes[0].set_ylabel('Mean pitch $p(t)$')
axes[0].set_title('(a) Cosmic cycle')
axes[0].set_ylim(0, 2.6)

# (b) Bifurcated Hubble parameter
H = 70 + 5*np.cos(2*np.pi*t_sim/100)
axes[1].plot(t_sim, H, lw=2, color='C1')
axes[1].axhline(73, color='C3', ls='--', label='Local $H_0$')
axes[1].axhline(67, color='C4', ls='--', label='CMB $H_0$')
axes[1].set_xlabel('Cosmic time (a.u.)')
axes[1].set_ylabel('$H$ (a.u.)')
axes[1].set_title('(b) Bifurcated Hubble parameter')
axes[1].legend(fontsize=8)

# (c) Phase diagram
omega = np.linspace(0.1, 5, 100)
F_eff = 1.0/omega - 0.5*omega**2
axes[2].plot(omega, F_eff, lw=2, color='C2')
axes[2].axhline(0, color='black', lw=0.5)
axes[2].fill_between(omega, F_eff, 0, where=(F_eff<0), alpha=0.3, color='C3', label='Repulsion')
axes[2].fill_between(omega, F_eff, 0, where=(F_eff>0), alpha=0.3, color='C0', label='Attraction')
axes[2].set_xlabel('Angular velocity $\\omega$')
axes[2].set_ylabel('Effective force')
axes[2].set_title('(c) Attraction vs. repulsion')
axes[2].legend(fontsize=8)

plt.tight_layout()
plt.savefig('figure3.pdf', bbox_inches='tight')
plt.close()

# ---------- Figure 4: Observational tests ----------
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# (a) Filament helicity
np.random.seed(42)
theta = np.linspace(0, 4*np.pi, 200)
r = np.linspace(1, 5, 200)
x = r*np.cos(theta)
y = r*np.sin(theta)
z = 0.5*theta
axes[0].plot(x, y, z, lw=2, color='C0')
axes[0].scatter(x[::20], y[::20], z[::20], c=z[::20], cmap='viridis', s=20)
axes[0].set_title('(a) Galaxy filament helicity')
axes[0].set_axis_off()

# (b) CMB B-mode spiral pattern
ax2 = fig.add_subplot(132, projection='polar')
phi = np.linspace(0, 4*np.pi, 400)
B = np.sin(3*phi)
ax2.plot(phi, 1+0.2*B, lw=2, color='C1')
ax2.set_title('(b) CMB spiral B-mode', pad=20)
ax2.set_rticks([])

# (c) Chiral Casimir experiment
axes[2].bar(['L-L', 'L-R', 'R-R'], [0.9, -0.8, 0.85], color=['C0','C3','C0'], alpha=0.7)
axes[2].axhline(0, color='black', lw=0.5)
axes[2].set_ylabel('Normalized force')
axes[2].set_title('(c) Chiral Casimir-like force')

plt.tight_layout()
plt.savefig('figure4.pdf', bbox_inches='tight')
plt.close()

print("Figures figure1.pdf ~ figure4.pdf generated successfully.")