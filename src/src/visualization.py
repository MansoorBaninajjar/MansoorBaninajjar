import matplotlib.pyplot as plt
from phasor_model import PhasorField

def plot_phasor_field(t=0.1, grid_size=200, profile='gaussian'):
    field = PhasorField(grid_size=grid_size, profile=profile)
    real, imag, amp = field.phasor_sum(t)

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    
    im0 = axs[0].imshow(real, extent=[-1, 1, -1, 1], cmap='RdBu')
    axs[0].set_title('Real Part of Ψ')
    plt.colorbar(im0, ax=axs[0])

    im1 = axs[1].imshow(imag, extent=[-1, 1, -1, 1], cmap='PuOr')
    axs[1].set_title('Imaginary Part of Ψ')
    plt.colorbar(im1, ax=axs[1])

    im2 = axs[2].imshow(amp, extent=[-1, 1, -1, 1], cmap='viridis')
    axs[2].set_title('Amplitude |Ψ|')
    plt.colorbar(im2, ax=axs[2])

    for ax in axs:
        ax.set_xlabel('x')
        ax.set_ylabel('y')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_phasor_field(t=0.2)
