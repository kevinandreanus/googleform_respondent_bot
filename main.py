from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Administrator/Desktop/chromedriver/chromedriver.exe')
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeEfhgzK6l-LL9zJSjCkUVxIoEB7fJjGDx_kumri_NxcViMJw/viewform')

radiobtn = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupEl")

# Radio Button [0, 1] Ya atau Tidak pernah
radiobtn[0].click()

submitbtn = driver.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
# Submit Page 1
submitbtn[0].click()

textinput = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")

# Nama
textinput[0].send_keys("Kevin Andreanus")

# Domisili
# Index 0: Jakbar || 1: JakTim || 2: JakUt || 3: JakSel || 4: JakPus || 5: Yang Lainnya (Extra Code)
domisili = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
domisili[4].click()

# Berapa Kali Mengunjungi
# Index 6: 1-2Kali || 7: 3-4Kali || 8: >5Kali
domisili[7].click()

# Jenis Kelamin
# Index 9: Laki-Laki || 10: Perempuan
domisili[9].click()

# Usia
# Index 11: 15-25Thn || 12: 26-35Thn || 13: 36-45Thn || 14: >45Thn
domisili[13].click()

# Pendidikan Terakhir
# Index 15: SMA/SMK || 16: D/S1 || 17: Yang Lain (Extra Code)
domisili[15].click()

# Profesi
# Index 18: Mahasiswa || 19: Karyawan || 20: Wirausaha || 21: Yang Lain (Extra Code)
domisili[19].click()

# Pendapatan
# Index 22: <2jt || 23: 2-4jt || 24: 4-8jt || 25: >8jt
domisili[25].click()

submit2 = driver.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
# Page 2 Submit
submit2[1].click()

# Merasa masakan sangat bersih
# Index 0, 1, 2, 3, 4
radio3 = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
radio3[3].click()

# Tekstur makanan baik
# Index 5, 6, 7, 8, 9
radio3[7].click()

# bahan segar
# index 10, 11, 12, 13, 14
radio3[13].click()

# tampilan menarik
# index 15, 16, 17, 18, 19
radio3[16].click()

# sesuai foto menu
# index 20, 21, 22, 23, 24
radio3[23].click()

# membangkitkan selera makan
# index 25, 26, 27, 28, 29
radio3[28].click()

# porsi standar
# index 30, 31, 32, 33, 34
radio3[33].click()

# sesuai selera
# index 35, 36, 37, 38, 39
radio3[37].click()

# rasa selalu sama
# index 40, 41, 42, 43, 44
radio3[42].click()

# makanan kalbar unik
# index 45, 46, 47, 48, 49
radio3[48].click()

# varian menu banyak
# index 50, 51, 52, 53, 54
radio3[53].click()

# makanan kalbar menarik
# index 55, 56, 57, 58, 59
radio3[57].click()

# sesuai selera saya
# index 60, 61, 62, 63, 64
radio3[62].click()

submit3 = driver.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
# Page 3 Submit
submit3[1].click()

# Merasa puas
# Index 0, 1, 2, 3, 4
radio4 = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
radio4[3].click()

# di pik pilihan utama
# Index 5, 6, 7, 8, 9
radio4[7].click()

# pelayanan baik
# index 10, 11, 12, 13, 14
radio4[13].click()

# pelayanan ramah
# index 15, 16, 17, 18, 19
radio4[16].click()

# rasa memenuhi harapan
# index 20, 21, 22, 23, 24
radio4[23].click()

# fasilitas sesuai harapan
# index 25, 26, 27, 28, 29
radio4[28].click()

# harga sesuai harapan
# index 30, 31, 32, 33, 34
radio4[33].click()

# kebersihan sesuai harapan
# index 35, 36, 37, 38, 39
radio4[37].click()

# tampilan memudahkan
# index 40, 41, 42, 43, 44
radio4[42].click()

# proses bayar mudah
# index 45, 46, 47, 48, 49
radio4[48].click()

# tempat parkir mudah
# index 50, 51, 52, 53, 54
radio4[53].click()

# penyajian cepat
# index 55, 56, 57, 58, 59
radio4[57].click()

submit4 = driver.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
# Page 4 Submit
submit4[1].click()