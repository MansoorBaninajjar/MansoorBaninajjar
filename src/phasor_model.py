import numpy as np

class PhasorField:
    def __init__(self, grid_size=100, omega=2*np.pi, profile='gaussian'):
        self.grid_size = grid_size
        self.omega = omega
        self.t = 0
        self.x = np.linspace(-1, 1, grid_size)
        self.y = np.linspace(-1, 1, grid_size)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        self.profile = self._amplitude_profile(profile)
    
    def _amplitude_profile(self, kind):
        R2 = self.X**2 + self.Y**2
        if kind == 'gaussian':
            return np.exp(-10 * R2)
        elif kind == 'ring':
            return np.exp(-100 * (R2 - 0.25)**2)
        elif kind == 'flat':
            return np.ones_like(R2)
        else:
            raise ValueError("Unknown profile type")
    
    def update(self, t):
        self.t = t
        phase = np.exp(1j * self.omega * t)
        return self.profile * phase
    
    def phasor_sum(self, t):
        wave = self.update(t)
        return np.real(wave), np.imag(wave), np.abs(wave)
