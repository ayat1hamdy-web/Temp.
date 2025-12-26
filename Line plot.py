import pandas as pd
import matplotlib.pyplot as plt

# 1. تحميل البيانات
# سنقرأ أول صفوف فقط للتجربة لأن الملف ضخم
df = pd.read_csv('Environment_Temperature_change_E_All_Data_NOFLAG.csv', encoding='ISO-8859-1')

# 2. تجهيز بيانات افتراضية لأسبوع (بناءً على طلب التاسك)
# لأن الملف يحتوي على بيانات سنوية، سنرسم درجات حرارة لأول 7 أيام من الأسبوع كمثال
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [22.5, 24.0, 21.8, 25.2, 23.9, 26.5, 25.0] # درجات حرارة تجريبية

# 3. إنشاء الرسم البياني (Line Plot)
plt.figure(figsize=(10, 6))
plt.plot(days, temperatures, marker='o', linestyle='-', color='b', linewidth=2)

# 4. إضافة العناوين والتسميات (Labels & Title)
plt.title('Temperature Variation Over a Week', fontsize=14)
plt.xlabel('Days of the Week', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# إضافة شبكة خلفية لتسهيل القراءة
plt.grid(True, linestyle='--', alpha=0.7)

# 5. عرض الرسم
plt.show()