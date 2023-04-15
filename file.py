import time
from plyer import notification

# Funksiya bildirişi göstərmək üçün
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Göz Rahatlığı Xatırlatıcısı',
        app_icon='yol/unvanı/icon.ico',
        timeout=5
    )

# Bildiriş göstərilməsi üçün təyin olunan zaman intervalı (saniyə)
interval = 1800 # 30 dəqiqə

while True:
    # Təyin olunan zaman intervalı gözləyin
    time.sleep(interval)
    # Bildirişi göstərin
    show_notification('Göz Rahatlığı Xatırlatıcısı', 'Maraqlarınızı üçün mərhələli olaraq mola verin!')
