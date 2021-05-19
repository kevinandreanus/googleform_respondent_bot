from selenium import webdriver
import random
import array as arr

driver = webdriver.Chrome(executable_path=r"C:/Users/Kevin/Desktop/googleform_respondent_bot/googleform_respondent_bot/chromedriver/chromedriver.exe")
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeEfhgzK6l-LL9zJSjCkUVxIoEB7fJjGDx_kumri_NxcViMJw/viewform')



namaarray = ["Michael Wijaya", "Tony Leonardi", "Ronald"]

for x in namaarray:

    radiobtn = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupEl")

    # Radio Button [0, 1] Ya atau Tidak pernah
    radiobtn[0].click()

    submitbtn = driver.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    # Submit Page 1
    submitbtn[0].click()

    textinput = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    textinput[0].send_keys(x)


    # Domisili
    # Index 0: Jakbar || 1: JakTim || 2: JakUt || 3: JakSel || 4: JakPus || 5: Yang Lainnya (Extra Code)
    domisili = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    acakdomisili = random.randint(0, 4)
    domisili[acakdomisili].click()

    # Berapa Kali Mengunjungi
    # Index 6: 1-2Kali || 7: 3-4Kali || 8: >5Kali
    acakmengunjungi = random.randint(6, 8)
    domisili[acakmengunjungi].click()

    # Jenis Kelamin
    # Index 9: Laki-Laki || 10: Perempuan
    acakjk = random.randint(9, 10)
    domisili[acakjk].click()

    # Usia
    # Index 11: 15-25Thn || 12: 26-35Thn || 13: 36-45Thn || 14: >45Thn
    acakusia = random.randint(11, 13)
    domisili[acakusia].click()

    # Pendidikan Terakhir
    # Index 15: SMA/SMK || 16: D/S1 || 17: Yang Lain (Extra Code)
    acakpend = random.randint(15, 16)
    domisili[acakpend].click()

    # Profesi
    # Index 18: Mahasiswa || 19: Karyawan || 20: Wirausaha || 21: Yang Lain (Extra Code)
    acakprof = random.randint(18, 20)
    domisili[acakprof].click()

    # Pendapatan
    # Index 22: <2jt || 23: 2-4jt || 24: 4-8jt || 25: >8jt
    acakpend = random.randint(22, 23)
    domisili[acakpend].click()

    submit2 = driver.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    # Page 2 Submit
    submit2[1].click()

    # Merasa masakan sangat bersih
    # Index 0, 1, 2, 3, 4
    radio3 = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    acak1 = random.randint(2, 4)
    radio3[acak1].click()

    # Tekstur makanan baik
    # Index 5, 6, 7, 8, 9
    acak2 = random.randint(7, 9)
    radio3[acak2].click()

    # bahan segar
    # index 10, 11, 12, 13, 14
    acak3 = random.randint(12,14)
    radio3[acak3].click()

    # tampilan menarik
    # index 15, 16, 17, 18, 19
    acak4 = random.randint(17, 19)
    radio3[acak4].click()

    # sesuai foto menu
    # index 20, 21, 22, 23, 24
    acak5 = random.randint(22, 24)
    radio3[acak5].click()

    # membangkitkan selera makan
    # index 25, 26, 27, 28, 29
    acak6 = random.randint(27, 29)
    radio3[acak6].click()

    # porsi standar
    # index 30, 31, 32, 33, 34
    acak7 = random.randint(32, 34)
    radio3[acak7].click()

    # sesuai selera
    # index 35, 36, 37, 38, 39
    acak8 = random.randint(37, 39)
    radio3[acak8].click()

    # rasa selalu sama
    # index 40, 41, 42, 43, 44
    acak9 = random.randint(42, 44)
    radio3[acak9].click()

    # makanan kalbar unik
    # index 45, 46, 47, 48, 49
    acak10 = random.randint(47, 49)
    radio3[acak10].click()

    # varian menu banyak
    # index 50, 51, 52, 53, 54
    acak11 = random.randint(52, 54)
    radio3[acak11].click()

    # makanan kalbar menarik
    # index 55, 56, 57, 58, 59
    acak12 = random.randint(57, 59)
    radio3[acak12].click()

    # sesuai selera saya
    # index 60, 61, 62, 63, 64
    acak13 = random.randint(62, 64)
    radio3[acak13].click()

    submit3 = driver.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    # Page 3 Submit
    submit3[1].click()

    # Merasa puas
    # Index 0, 1, 2, 3, 4
    radio4 = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    acak20 = random.randint(2, 4)
    radio4[acak20].click()

    # di pik pilihan utama
    # Index 5, 6, 7, 8, 9
    acak21 = random.randint(7, 9)
    radio4[acak21].click()

    # pelayanan baik
    # index 10, 11, 12, 13, 14
    acak22 = random.randint(12, 14)
    radio4[acak22].click()

    # pelayanan ramah
    # index 15, 16, 17, 18, 19
    acak23 = random.randint(17, 19)
    radio4[acak23].click()

    # rasa memenuhi harapan
    # index 20, 21, 22, 23, 24
    acak24 = random.randint(22, 24)
    radio4[acak24].click()

    # fasilitas sesuai harapan
    # index 25, 26, 27, 28, 29
    acak25 = random.randint(27, 29)
    radio4[acak25].click()

    # harga sesuai harapan
    # index 30, 31, 32, 33, 34
    acak26 = random.randint(32, 34)
    radio4[acak26].click()

    # kebersihan sesuai harapan
    # index 35, 36, 37, 38, 39
    acak27 = random.randint(37, 39)
    radio4[acak27].click()

    # tampilan memudahkan
    # index 40, 41, 42, 43, 44
    acak28 = random.randint(42, 44)
    radio4[acak28].click()

    # proses bayar mudah
    # index 45, 46, 47, 48, 49
    acak29 = random.randint(47, 49)
    radio4[acak29].click()

    # tempat parkir mudah
    # index 50, 51, 52, 53, 54
    acak30 = random.randint(52, 54)
    radio4[acak30].click()

    # penyajian cepat
    # index 55, 56, 57, 58, 59
    acak31 = random.randint(57, 59)
    radio4[acak31].click()

    submit4 = driver.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    # Page 4 Submit
    submit4[1].click()

    print("Response Complete, Name: " + x)

    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeEfhgzK6l-LL9zJSjCkUVxIoEB7fJjGDx_kumri_NxcViMJw/viewform')