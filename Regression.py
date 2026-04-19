import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Обработка таблицы
df = pd.read_excel('D:\Работа\Тестовое PowerBI\тестовое задание для стажера в ИТ.xlsx', sheet_name='БД_объем')
df["Месяц"] = df["дата"].dt.month
df["Год"] = df["дата"].dt.year

# Считаем продажи по месяцам
monthly_sales = df.groupby(["Год", "Месяц"])["Объем_дал"].sum().reset_index()
monthly_sales["Лето"] = monthly_sales["Месяц"].isin([6,7,8]).astype(int)
monthly_sales["sin_month"] = np.sin(2 * np.pi * monthly_sales["Месяц"] / 12)
monthly_sales["cos_month"] = np.cos(2 * np.pi * monthly_sales["Месяц"] / 12)
print(monthly_sales)

# Температуры за 2022 год
temp_2022 = pd.DataFrame({
    "Год": [2022]*12,
    "Месяц": list(range(1,13)),
    "Температура": [-2.1, 0.3, 1.1, 5.7, 11.6, 19.0, 18.4, 20.8, 10.4, 8.9, 2.0, -2.8]
})

# Температуры за 2023 год (до августа)
temp_2023 = pd.DataFrame({
    "Год": [2023]*8,
    "Месяц": list(range(1,9)),
    "Температура": [-0.7, -1.4, 2.7, 8.8, 13.0, 17.7, 18.6, 20.7]
})

temp_data = pd.concat([temp_2022, temp_2023], ignore_index=True)
monthly_sales = monthly_sales.merge(temp_data, on=["Год","Месяц"], how="left")
monthly_sales["Номер_месяца"] = range(1, len(monthly_sales)+1)

# Удаляем август 2023, так как там неполные данные
monthly_sales = monthly_sales[~((monthly_sales["Год"] == 2023) & (monthly_sales["Месяц"] == 8))]
monthly_sales["Номер_месяца"] = range(1, len(monthly_sales)+1)

# Строим модель
X = monthly_sales[["Лето", "sin_month", "cos_month", "Температура", "Номер_месяца"]]
y = monthly_sales["Объем_дал"]
model = LinearRegression()
model.fit(X, y)

# Выводим полученные коэффициенты и коэффициент кореляции
print("Коэффициенты:", model.coef_)
print("Свободный член:", model.intercept_)
print("R^2:", model.score(X, y))

# Добавляем прогноз
monthly_sales["Прогноз"] = model.predict(X)
future_months = pd.DataFrame({
    "Год": [2023]*4 + [2024]*12,
    "Месяц": [9, 10, 11, 12] + list(range(1,13))
})

future_months["Лето"] = future_months["Месяц"].isin([6,7,8]).astype(int)
future_months["sin_month"] = np.sin(2 * np.pi * future_months["Месяц"] / 12)
future_months["cos_month"] = np.cos(2 * np.pi * future_months["Месяц"] / 12)
future_months["Номер_месяца"] = range(len(monthly_sales)+1, len(monthly_sales)+len(future_months)+1)

temps_2023 = [16.2, 8.0, 1.9, -0.7]
temps_2024 = [-5.1, 1.7, 4.1, 10.1, 14.9, 18.9, 21.0, 19.9, 17.5, 8.3, 2.6, 0.3]
future_months["Температура"] = temps_2023 + temps_2024

future_months["Прогноз"] = model.predict(
    future_months[["Лето","sin_month","cos_month","Температура","Номер_месяца"]]
)
all_data = pd.concat([monthly_sales, future_months], ignore_index=True)

# Визуализируем данные
plt.figure(figsize=(12,6))
plt.plot(monthly_sales["Номер_месяца"], monthly_sales["Объем_дал"], marker="o", label="Фактический объем продаж")
plt.plot(all_data["Номер_месяца"], all_data["Прогноз"], marker="o", label="Прогноз")
plt.xlabel("Номер месяца (с января 2022)")
plt.ylabel("Сумма продаж")
plt.title("Прогноз продаж (до конца 2024)")
plt.legend()
plt.grid(True)
plt.show()