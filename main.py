import matplotlib.pyplot as plt
import numpy as np
from utils import pan_tompkins


data = np.loadtxt("data/a1Саня.asc", skiprows=4)
# emg_signal = data
eeg = data
fs = 5000
# Детектируем острые пики
peak_locs = pan_tompkins(eeg, fs)
print(len(peak_locs))

# построение графика сигнала ЭЭГ
plt.plot(eeg)

# наложение маркеров для острых пиков
plt.scatter(peak_locs, eeg[peak_locs], c='r', marker='o')

# добавление названий осей и заголовка
plt.xlabel('Отсчеты')
plt.ylabel('Амплитуда')
plt.title('Острые пики ЭЭГ')
plt.show()