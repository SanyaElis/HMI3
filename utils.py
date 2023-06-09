import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def pan_tompkins(ecg, fs):
    # Нормализуем сигнал
    ecg = (ecg - np.mean(ecg)) / np.std(ecg)

    # Находим производную сигнала
    derivative = np.gradient(ecg)

    # Применяем низкочастотный фильтр
    b, a = signal.butter(2, 5 / (fs / 2), 'low')
    filtered_ecg = signal.filtfilt(b, a, derivative)

    # Применяем высокочастотный фильтр
    b, a = signal.butter(2, 0.5 / (fs / 2), 'high')
    filtered_ecg = signal.filtfilt(b, a, filtered_ecg)

    # Находим порог для детекции острых пиков
    std_dev = np.std(filtered_ecg)
    # threshold = 0.2 * std_dev
    threshold = z_score_threshold(filtered_ecg, 1.4)

    # plt.plot(filtered_ecg)


    # # добавление названий осей и заголовка
    # plt.xlabel('Отсчеты')
    # plt.ylabel('Амплитуда')
    # plt.title('Острые пики ЭЭГ')
    # plt.show()

    # Детектируем острые пики
    peak_locs = []
    for i in range(1, len(filtered_ecg) - 1):
        if (filtered_ecg[i] > threshold) and (filtered_ecg[i] > filtered_ecg[i - 1]) and (
                filtered_ecg[i] > filtered_ecg[i + 1]):
            peak_locs.append(i)

    # plt.scatter(peak_locs, filtered_ecg[peak_locs], c='r', marker='o')
    # plt.show()
    return peak_locs


def read_data(file_path):
    data = np.loadtxt(file_path, skiprows=4)
    # if isinstance(data[0], (list, tuple, np.ndarray)):
    #     return data[:, 1]
    return data


# Определяем порог на основе метода Z-оценки
def z_score_threshold(data, n_std):
    threshold = np.mean(data) + n_std * np.std(data)
    return threshold


# Определяем порог вручную
def manual_threshold(data, std_factor):
    threshold = np.mean(data) + std_factor * np.std(data)
    return threshold



