import smtplib

conn = smtplib.SMTP('smtp.gmail.com' , 587) #Kurulum başlangıcı ve önerilen 587. port (Gmail için çalışacağı unutulmamalı)
conn.ehlo()
conn.starttls()

conn.login('e posta' , 'sifre') #Giriş komutu

conn.sendmail('gönderen e postası' , 'alıcı e postası', 'Subject: Mail konusu\n\n Buraya mailinizi yazınız')
#\n newline komutudur. Tek satır üzerinde çalışma yapabilmenizi sağlar.
#Mail gönderirken Türkçe karakter kullanamıyorsunuz bu ASCII'den kaynaklı bir sıkıntı.
#Bu kod üzerinden gmail hesabınıza giriş yapmaya çalışırsanız güvenilirlik düşük olduğu için hata verecek.
#Bu yüzden gmail ayalarınızdan düşük güvenlikli girişlere izin vermelisiniz.
conn.quit()
