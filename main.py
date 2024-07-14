import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
#from playsound import playsound

from test import Ui_MainWindow
from calculate_page import Ui_Form
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # the way app working
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.score = 0
        #Khai bao dong ho dem nguoc

        self.my_qtimer = QTimer(self)
        self.startWatch = False

        self.widget_counter_int = None
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.uic.textEdit.setText("00:00:00")
        self.uic.textEdit.setAlignment(Qt.AlignHCenter)
        self.uic.Start_Button.clicked.connect(self.timer_start)

        self.uic.Clear_Button.clicked.connect(self.time_clear)
        self.uic.BackStudyWithMe.clicked.connect(self.BackToMenu)

        #Login
        self.uic.Login_Button.clicked.connect(self.loginButton)
        self.uic.BackLogin_Button.clicked.connect(self.backLogin)
        #MENU
        # khai bao nut MON HOC
        self.uic.Subject.clicked.connect(self.openSubject)

        # Khai bao nut BACK
        self.uic.Back.clicked.connect(self.BackToMenu)
        self.uic.StudyWithMe.clicked.connect(self.openStudyWithMe)

        ################# Máy tính ############################
        #self.cal.Number0.clicked.connect(lambda: self.pressed_it("0"))
        #T####################RAC NGHIEM#######################
        self.uic.TracNghiem_Button.clicked.connect(self.openTracNghiemPage)
        self.uic.BackTracNghiem.clicked.connect(self.BackToMenu)
        self.uic.KTGK_GDCD.clicked.connect(self.openKTGKI_GDCD)
        self.uic.BackTracNghiem_GDCD.clicked.connect(self.openTracNghiemPage)
        self.uic.GDCDBT.clicked.connect(self.openTracNghiemGDCD)
        self.uic.KTGKI_GDCD_Back.clicked.connect(self.openTracNghiemGDCD)
        self.uic.KTGKI_GDCD_Button.clicked.connect(self.KTGKI_GDCD)
        self.uic.KTGKI_GDCD_Button.clicked.connect(self.timer_start2)

        self.uic.Next_Button_GDCD1.clicked.connect(self.Question2_KTGKI_GDCD_Page)
        self.uic.Next_Button_GDCD1.clicked.connect(self.timer_start3)

        self.uic.Next_Button_GDCD2.clicked.connect(self.Question3_KTGKI_GDCD_Page)
        self.uic.Next_Button_GDCD2.clicked.connect(self.timer_start4)

        self.uic.Next_Button_GDCD3.clicked.connect(self.Question4_KTGKI_GDCD_Page)
        self.uic.Next_Button_GDCD3.clicked.connect(self.timer_start5)

        self.uic.Next_Button_GDCD4.clicked.connect(self.Question5_KTGKI_GDCD_Page)
        self.uic.Next_Button_GDCD4.clicked.connect(self.timer_start6)

        self.uic.Next_Button_GDCD5.clicked.connect(self.Question6_KTGKI_GDCD_Page)
        self.uic.Next_Button_GDCD5.clicked.connect(self.timer_start7)

        self.uic.Next_Button_GDCD6.clicked.connect(self.Question7_KTGKI_GDCD_Page)
        self.uic.Next_Button_GDCD6.clicked.connect(self.timer_start8)

        self.uic.Next_Button_GDCD7.clicked.connect(self.Question8_KTGKI_GDCD_Page)
        self.uic.Next_Button_GDCD7.clicked.connect(self.timer_start9)

        self.uic.Next_Button_GDCD8.clicked.connect(self.Question9_KTGKI_GDCD_Page)
        self.uic.Next_Button_GDCD8.clicked.connect(self.timer_start10)

        self.uic.Next_Button_GDCD9.clicked.connect(self.Question10_KTGKI_GDCD_Page)
        self.uic.Next_Button_GDCD9.clicked.connect(self.timer_start11)

        self.uic.Next_Button_GDCD10.clicked.connect(self.openResult_Page)

        self.uic.Back_Result.clicked.connect(self.openTracNghiemPage)

        #Muc Toan
        #Khai bao nut vao Math
        self.uic.Math.clicked.connect(self.openMath)
        #Khai bao nut vao Dai So
        self.uic.DaiSoButton.clicked.connect(self.JustForDaiSoButton)
        self.uic.HinhHocButton.clicked.connect(self.openHinhHoc)
        self.uic.HinhHocLyThuyetButton.clicked.connect(self.openHinhHocLyThuyet_page)
        #Khai bao nut vao Ly Thuyet Dai So
        self.uic.DaiSoLyThuyetButton.clicked.connect(self.openLyThuyetDaiSo)
        #Khai bao nut vao Bai Tap Dai SO

        #GDCD
        self.uic.GDCD.clicked.connect(self.openGDCD_page)
        #Khai bao nut vao Bai 1 dai so
        self.uic.Chuong1Bai1.clicked.connect(self.openDaiSoChuong1Bai1)
        #self.uic.Chuong1Bai1_2.clicked.connect(self.openBTDaiSoChuong1Bai1)

        self.uic.Chuong2Bai1.clicked.connect(self.openDaiSoChuong2Bai1)
        #self.uic.Chuong2Bai1_2.clicked.connect(self.openBTDaiSoChuong2Bai1)

        self.uic.Chuong3Bai1.clicked.connect(self.openDaiSoChuong3Bai1)
    #    self.uic.Chuong3Bai1_2.clicked.connect(self.openBTDaiSoChuong3Bai1)

        self.uic.Chuong4Bai1.clicked.connect(self.openDaiSoChuong4Bai1)
    #    self.uic.Chuong4Bai1_3.clicked.connect(self.openBTDaiSoChuong4Bai1)

        self.uic.Chuong5Bai1.clicked.connect(self.openDaiSoChuong5Bai1)
    #    self.uic.Chuong5Bai1_3.clicked.connect(self.openBTDaiSoChuong5Bai1)

        #Khai bao nut vao Bai 2 dai so
        self.uic.Chuong1Bai2.clicked.connect(self.openDaiSoChuong1Bai2)
        #self.uic.Chuong1Bai2_2.clicked.connect(self.openBTDaiSoChuong1Bai2)

        self.uic.Chuong2Bai2.clicked.connect(self.openDaiSoChuong2Bai2)
        #self.uic.Chuong2Bai2_2.clicked.connect(self.openBTDaiSoChuong2Bai2)

        self.uic.Chuong3Bai2.clicked.connect(self.openDaiSoChuong3Bai2)
    #    self.uic.Chuong3Bai2_2.clicked.connect(self.openBTDaiSoChuong3Bai2)

        self.uic.Chuong4Bai2.clicked.connect(self.openDaiSoChuong4Bai2)
    #    self.uic.Chuong4Bai2_3.clicked.connect(self.openBTDaiSoChuong4Bai2)

        self.uic.Chuong5Bai2.clicked.connect(self.openDaiSoChuong5Bai2)
    #    self.uic.Chuong5Bai2_3.clicked.connect(self.openBTDaiSoChuong5Bai2)

        # Khai bao nut vao Bai 3 dai so
        self.uic.Chuong1Bai3.clicked.connect(self.openDaiSoChuong1Bai3)
        #self.uic.Chuong1Bai3_2.clicked.connect(self.openBTDaiSoChuong1Bai3)

        self.uic.Chuong2Bai3.clicked.connect(self.openDaiSoChuong2Bai3)
        #self.uic.Chuong2Bai3_2.clicked.connect(self.openBTDaiSoChuong2Bai3)

        self.uic.Chuong3Bai3.clicked.connect(self.openDaiSoChuong3Bai3)
    #    self.uic.Chuong3Bai3_2.clicked.connect(self.openBTDaiSoChuong3Bai3)

        self.uic.Chuong4Bai3.clicked.connect(self.openDaiSoChuong4Bai3)
    #    self.uic.Chuong4Bai3_3.clicked.connect(self.openBTDaiSoChuong4Bai3)

        self.uic.Chuong5Bai3.clicked.connect(self.openDaiSoChuong5Bai3)
    #    self.uic.Chuong5Bai3_3.clicked.connect(self.openBTDaiSoChuong5Bai3)

        # Khai bao nut vao Bai 4 dai so
        self.uic.Chuong2Bai4.clicked.connect(self.openDaiSoChuong2Bai4)
        #self.uic.Chuong2Bai4_2.clicked.connect(self.openBTDaiSoChuong2Bai4)

        self.uic.Chuong3Bai4.clicked.connect(self.openDaiSoChuong3Bai4)
    #    self.uic.Chuong3Bai4_2.clicked.connect(self.openBTDaiSoChuong3Bai4)

        self.uic.Chuong5Bai4.clicked.connect(self.openDaiSoChuong5Bai4)
    #    self.uic.Chuong5Bai4_3.clicked.connect(self.openBTDaiSoChuong5Bai4)

        # Khai bao nut vao Bai 5 dai so
        self.uic.Chuong2Bai5.clicked.connect(self.openDaiSoChuong2Bai5)
        #self.uic.Chuong2Bai5_2.clicked.connect(self.openBTDaiSoChuong2Bai5)

        self.uic.Chuong5Bai5.clicked.connect(self.openDaiSoChuong5Bai5)
    #    self.uic.Chuong5Bai5_3.clicked.connect(self.openBTDaiSoChuong5Bai5)

        #Khai bao nut back cua Toan
        self.uic.Back5.clicked.connect(self.openSubject)
        #Khai bao nut back cua Dai So
        self.uic.Back3.clicked.connect(self.openMath)
        self.uic.Back3_2.clicked.connect(self.openMath)
        #Khai bao nut back cua Ly Thuyet Dai So
        self.uic.Back6.clicked.connect(self.JustForDaiSoButton)
        #Khai bao nut back cua Bai tap dai so
        self.uic.Back6_2.clicked.connect(self.openHinhHoc)
        #Khai bao nut back cua Bai Tap Dai So

        #Khai bao nut back Bai dai so
        self.uic.Back8.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_2.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_3.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_4.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_5.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_6.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_7.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_8.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_9.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_10.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_11.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_12.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_13.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_14.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_15.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_16.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_17.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_18.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back9_19.clicked.connect(self.openLyThuyetDaiSo)
        self.uic.Back10_9.clicked.connect(self.openBaiTapDaiSo)

        self.uic.Chuong1Bai1_2.clicked.connect(self.openHinhHoc_Bai1)
        self.uic.Chuong1Bai2_2.clicked.connect(self.openHinhHoc_Bai2)
        self.uic.Chuong1Bai3_2.clicked.connect(self.openHinhHoc_Bai3)
        self.uic.Chuong1Bai4_2.clicked.connect(self.openHinhHoc_Bai4)
        self.uic.Chuong1Bai5_2.clicked.connect(self.openHinhHoc_Bai5)
        self.uic.Chuong1Bai6_2.clicked.connect(self.openHinhHoc_Bai6)
        self.uic.Chuong1Bai7_2.clicked.connect(self.openHinhHoc_Bai7)
        self.uic.Chuong2Bai1_2.clicked.connect(self.openHinhHoc_Bai8)
        self.uic.Chuong2Bai2_2.clicked.connect(self.openHinhHoc_Bai9)
        self.uic.Chuong2Bai3_2.clicked.connect(self.openHinhHoc_Bai10)
        self.uic.Chuong2Bai4_2.clicked.connect(self.openHinhHoc_Bai11)
        self.uic.Chuong2Bai5_2.clicked.connect(self.openHinhHoc_Bai12)
        self.uic.Chuong3Bai1_2.clicked.connect(self.openHinhHoc_Bai13)
        self.uic.Chuong3Bai2_2.clicked.connect(self.openHinhHoc_Bai14)
        self.uic.Chuong3Bai3_2.clicked.connect(self.openHinhHoc_Bai15)
        self.uic.Chuong3Bai4_2.clicked.connect(self.openHinhHoc_Bai16)
        self.uic.Chuong3Bai5_2.clicked.connect(self.openHinhHoc_Bai17)

        #Back Tin
        self.uic.BackIT.clicked.connect(self.openSubject)
        self.uic.BackIT_2.clicked.connect(self.openIT_page)
        self.uic.BackIT_3.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_4.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_5.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_6.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_7.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_8.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_9.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_10.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_11.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_12.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_13.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_14.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_15.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_16.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_17.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_18.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_19.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_20.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_21.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_22.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_23.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_24.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_25.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_26.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_27.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_28.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_29.clicked.connect(self.openIT_page_2)
        self.uic.BackIT_30.clicked.connect(self.openIT_page)
        self.uic.BackIT_31.clicked.connect(self.openBaitapTinCoBan_page)
        self.uic.BackIT_32.clicked.connect(self.openBaitapTinCoBan_page_2)
        self.uic.BackIT_33.clicked.connect(self.openBaitapTinCoBan_page_2)
        self.uic.BackIT_34.clicked.connect(self.openBaitapTinCoBan_page_2)

        self.uic.BackIT_36.clicked.connect(self.openBaitapTinCoBan_page_2)
        self.uic.BackIT_37.clicked.connect(self.openBaitapTinCoBan_page)
        self.uic.BackIT_38.clicked.connect(self.openDapanTinCoBan_page)
        self.uic.BackIT_39.clicked.connect(self.openDapanTinCoBan_page)
        self.uic.BackIT_40.clicked.connect(self.openDapanTinCoBan_page)

        self.uic.BackIT_82.clicked.connect(self.openDapanTinCoBan_page)
        self.uic.BackIT_83.clicked.connect(self.openIT_page)
        self.uic.BackIT_84.clicked.connect(self.openBaiTapNangCaoIT_page)
        self.uic.BackIT_85.clicked.connect(self.openBaiTapNangCaoIT_page)
        self.uic.BackIT_86.clicked.connect(self.openBaiTapNangCaoIT_page)
        self.uic.BackIT_87.clicked.connect(self.openBaiTapNangCaoIT_page)

        self.uic.DaiSoBaiTapButton.clicked.connect(self.openBTDaiSo)
        self.uic.HinhHocBaiTapButton.clicked.connect(self.openBTHinhHoc)
        self.uic.BackGDCD.clicked.connect(self.openSubject)
        self.uic.BackGDCD_2.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_3.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_4.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_5.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_6.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_7.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_8.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_9.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_10.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_11.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_12.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_13.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_14.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_15.clicked.connect(self.openGDCD_page)
        self.uic.BackGDCD_16.clicked.connect(self.openGDCD_page)

        self.uic.Back8_2.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_3.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_4.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_5.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_6.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_7.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_8.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_9.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_10.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_11.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_12.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_13.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_14.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_15.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_16.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_17.clicked.connect(self.openHinhHocLyThuyet_page)
        self.uic.Back8_18.clicked.connect(self.openHinhHocLyThuyet_page)

        self.uic.BackBTMath.clicked.connect(self.openDaiSo_2)
        self.uic.BackBTMath_2.clicked.connect(self.openHinhHoc)
        self.uic.BackBTMath_3.clicked.connect(self.openDapanTinCoBan_page)
        self.uic.BackBTMath_4.clicked.connect(self.openBaitapTinCoBan_page)


    # Back của văn
        self.uic.Literature.clicked.connect(self.openVan_Page)
        self.uic.BackVan.clicked.connect(self.openSubject)
        self.uic.BackVanBai1.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai2.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai3.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai4.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai5.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai6.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai7.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai8.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai9.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai10.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai11.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai12.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai13.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai14.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai15.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai16.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai17.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai18.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai19.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai20.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai21.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai22.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai23.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai24.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai25.clicked.connect(self.openVan_Page)
        self.uic.BackVanBai26.clicked.connect(self.openVan_Page)

        self.uic.VanBai1.clicked.connect(self.openBai1Van)
        self.uic.VanBai2.clicked.connect(self.openBai2Van)
        self.uic.VanBai3.clicked.connect(self.openBai3Van)
        self.uic.VanBai4.clicked.connect(self.openBai4Van)
        self.uic.VanBai5.clicked.connect(self.openBai5Van)
        self.uic.VanBai6.clicked.connect(self.openBai6Van)
        self.uic.VanBai7.clicked.connect(self.openBai7Van)
        self.uic.VanBai8.clicked.connect(self.openBai8Van)
        self.uic.VanBai9.clicked.connect(self.openBai9Van)
        self.uic.VanBai10.clicked.connect(self.openBai10Van)
        self.uic.VanBai11.clicked.connect(self.openBai11Van)
        self.uic.VanBai12.clicked.connect(self.openBai12Van)
        self.uic.VanBai13.clicked.connect(self.openBai13Van)
        self.uic.VanBai14.clicked.connect(self.openBai14Van)
        self.uic.VanBai15.clicked.connect(self.openBai15Van)
        self.uic.VanBai16.clicked.connect(self.openBai16Van)
        self.uic.VanBai17.clicked.connect(self.openBai17Van)
        self.uic.VanBai18.clicked.connect(self.openBai18Van)
        self.uic.VanBai19.clicked.connect(self.openBai19Van)
        self.uic.VanBai20.clicked.connect(self.openBai20Van)
        self.uic.VanBai21.clicked.connect(self.openBai21Van)
        self.uic.VanBai22.clicked.connect(self.openBai22Van)
        self.uic.VanBai23.clicked.connect(self.openBai23Van)
        self.uic.VanBai24.clicked.connect(self.openBai24Van)
        self.uic.VanBai25.clicked.connect(self.openBai25Van)
        self.uic.VanBai26.clicked.connect(self.openBai26Van)

    #DANG CAP NHAT


#GDCD
        self.uic.Bai1GDCD.clicked.connect(self.openBai1GDCD)
        self.uic.Bai2GDCD.clicked.connect(self.openBai2GDCD)
        self.uic.Bai3GDCD.clicked.connect(self.openBai3GDCD)
        self.uic.Bai4GDCD.clicked.connect(self.openBai4GDCD)
        self.uic.Bai5GDCD.clicked.connect(self.openBai5GDCD)
        self.uic.Bai6GDCD.clicked.connect(self.openBai6GDCD)
        self.uic.Bai7GDCD.clicked.connect(self.openBai7GDCD)
        self.uic.Bai8GDCD.clicked.connect(self.openBai8GDCD)
        self.uic.Bai9GDCD.clicked.connect(self.openBai9GDCD)
        self.uic.Bai10GDCD.clicked.connect(self.openBai10GDCD)
        self.uic.Bai11GDCD.clicked.connect(self.openBai11GDCD)
        self.uic.Bai12GDCD.clicked.connect(self.openBai12GDCD)
        self.uic.Bai13GDCD.clicked.connect(self.openBai13GDCD)
        self.uic.Bai14GDCD.clicked.connect(self.openBai14GDCD)
        self.uic.Bai16GDCD.clicked.connect(self.openBai15GDCD)

#TIN HOC
        #khai bao nut tin hoc
        self.uic.IT.clicked.connect(self.openIT_page)
        self.uic.LyThuyetITButton.clicked.connect(self.openChuongTrinhHocChinhIT)

        #Bai hoc
        self.uic.Bai1IT.clicked.connect(self.openBai1IT)
        self.uic.Bai2IT.clicked.connect(self.openBai2IT)
        self.uic.Bai3IT.clicked.connect(self.openBai3IT)
        self.uic.Bai4IT.clicked.connect(self.openBai4IT)
        self.uic.Bai5IT.clicked.connect(self.openBai5IT)
        self.uic.Bai6IT.clicked.connect(self.openBai6IT)
        self.uic.Bai7IT.clicked.connect(self.openBai7IT)
        self.uic.Bai8IT.clicked.connect(self.openBai8IT)
        self.uic.Bai9IT.clicked.connect(self.openBai9IT)
        self.uic.Bai10IT.clicked.connect(self.openBai10IT)
        self.uic.Bai11IT.clicked.connect(self.openBai11IT)
        self.uic.Bai12IT.clicked.connect(self.openBai12IT)
        self.uic.Bai13IT.clicked.connect(self.openBai13IT)
        self.uic.Bai14IT.clicked.connect(self.openBai14IT)
        self.uic.Bai15IT.clicked.connect(self.openBai15IT)
        self.uic.Bai16IT.clicked.connect(self.openBai16IT)
        self.uic.Bai17IT.clicked.connect(self.openBai17IT)
        self.uic.Bai18IT.clicked.connect(self.openBai18IT)
        self.uic.Bai19IT.clicked.connect(self.openBai19IT)
        self.uic.Thuchanh1.clicked.connect(self.openThuchanh1)
        self.uic.Thuchanh2.clicked.connect(self.openThuchanh2)
        self.uic.Thuchanh3.clicked.connect(self.openThuchanh3)
        self.uic.Thuchanh4.clicked.connect(self.openThuchanh4)
        self.uic.Thuchanh5.clicked.connect(self.openThuchanh5)
        self.uic.Thuchanh6.clicked.connect(self.openThuchanh6)
        self.uic.Thuchanh7.clicked.connect(self.openThuchanh7)
        self.uic.Thuchanh8.clicked.connect(self.openThuchanh8)
        self.uic.BaiTapITButton.clicked.connect(self.openBaitapTinCoBan_page)
        self.uic.BaiTapITButton_2.clicked.connect(self.openBaitapTinCoBan_page_2)
        self.uic.BaiTapITButton_3.clicked.connect(self.openDapanTinCoBan_page)
        #Cau hoi
        self.uic.Chuong2IT.clicked.connect(self.openChuong2IT_page)
        self.uic.Chuong3IT.clicked.connect(self.openChuong3IT_page)
        self.uic.Chuong4IT.clicked.connect(self.openChuong4IT_page)
        self.uic.Chuong5IT.clicked.connect(self.openChuong5IT_page)
        self.uic.Chuong6IT.clicked.connect(self.openChuong6IT_page)
        #Dap an
        self.uic.Chuong2IT_2.clicked.connect(self.openChuong2IT_page_3)
        self.uic.Chuong3IT_2.clicked.connect(self.openChuong3IT_page_3)
        self.uic.Chuong4IT_2.clicked.connect(self.openChuong4IT_page_3)
        self.uic.Chuong5IT_2.clicked.connect(self.openChuong5IT_page_3)
        self.uic.Chuong6IT_2.clicked.connect(self.openChuong6IT_page_3)

        self.uic.BaiTapNangCaoITButton.clicked.connect(self.openBaiTapNangCaoIT_page)
        self.uic.Chuyende1_1.clicked.connect(self.openKiemtramangchanle)
        self.uic.Chuyende1_2.clicked.connect(self.openBaitoanlaybi)
        self.uic.Chuyende1_3.clicked.connect(self.openMangsongaunhien)
        self.uic.Chuyende2_1.clicked.connect(self.openDoisothapphannhiphan)


#English
        self.uic.English.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish.clicked.connect(self.openSubject)
        self.uic.BackEnglish_2.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish_3.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish_4.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish_5.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish_6.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish_7.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish_8.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish_9.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish_10.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish_11.clicked.connect(self.openEnglishPage)
        self.uic.BackEnglish_12.clicked.connect(self.openEnglishPage)

        self.uic.Bidong.clicked.connect(self.openBidongPage)
        self.uic.Daitunhanxung.clicked.connect(self.openDaitunhanxungPage)
        self.uic.Cauhoiduoi.clicked.connect(self.openCauhoiduoiPage)
        self.uic.Hientaidon.clicked.connect(self.openHientaidonPage)
        self.uic.Hientaitiepdien.clicked.connect(self.openHientaitiepdienPage)
        self.uic.Hientaihoanthanh.clicked.connect(self.openHientaihoanthanhPage)
        self.uic.Quakhudon.clicked.connect(self.openQuakhudonPage)
        self.uic.Quakhutiepdien.clicked.connect(self.openQuakhutiepdien)
        self.uic.Quakhuhoanthanh.clicked.connect(self.openQuakhuhoanthanhPage)
        self.uic.Tuonglaidon.clicked.connect(self.openTuonglaidonPage)
        self.uic.Tuonglaitiepdien.clicked.connect(self.openTuonglaitiepdienPage)

        self.count = 0
        self.total_seconds = 0

        self.uic.Calculate.clicked.connect(self.open_Cal)
############################################################
    def open_Cal(self):
        self.Calculate_page_var = QtWidgets.QMainWindow()
        self.cal = Ui_Form()
        self.cal.setupUi(self.Calculate_page_var)
        self.Calculate_page_var.show()

        self.cal.Number0.clicked.connect(lambda: self.pressed_it("0"))
        self.cal.Number1.clicked.connect(lambda: self.pressed_it("1"))
        self.cal.Number2.clicked.connect(lambda: self.pressed_it("2"))
        self.cal.Number3.clicked.connect(lambda: self.pressed_it("3"))
        self.cal.Number4.clicked.connect(lambda: self.pressed_it("4"))
        self.cal.Number5.clicked.connect(lambda: self.pressed_it("5"))
        self.cal.Number6.clicked.connect(lambda: self.pressed_it("6"))
        self.cal.Number7.clicked.connect(lambda: self.pressed_it("7"))
        self.cal.Number8.clicked.connect(lambda: self.pressed_it("8"))
        self.cal.Number9.clicked.connect(lambda: self.pressed_it("9"))
        self.cal.Percent_Button.clicked.connect(lambda: self.pressed_it("%"))
        self.cal.Div_Button.clicked.connect(lambda: self.pressed_it("/"))
        self.cal.Dot_Button.clicked.connect(lambda: self.pressed_it("."))
        self.cal.Minus_Button.clicked.connect(lambda: self.pressed_it("-"))
        self.cal.Add_Button.clicked.connect(lambda: self.pressed_it("+"))
        self.cal.Multiply_Button.clicked.connect(lambda: self.pressed_it("*"))
        self.cal.AC_Button.clicked.connect(lambda: self.pressed_it("AC"))
        self.cal.Arrow_Button.clicked.connect(lambda: self.pressed_del())
        self.cal.Equal_Button.clicked.connect(lambda: self.pressed_Equal())
        self.cal.Change_Button.clicked.connect(lambda: self.pressed_Change())

    def openVan_Page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Van_Page)
    def openBai1Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai1_Page)
    def openBai2Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai2_Page)
    def openBai3Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai3_Page)
    def openBai4Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai4_Page)
    def openBai5Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai5_Page)
    def openBai6Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai6_Page)
    def openBai7Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai7_Page)
    def openBai8Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai8_Page)
    def openBai9Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai9_Page)
    def openBai10Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai10_Page)
    def openBai11Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai11_Page)
    def openBai12Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai12_Page)
    def openBai13Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai13_Page)
    def openBai14Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai14_Page)
    def openBai15Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai15_Page)
    def openBai16Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai16_Page)
    def openBai17Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai17_Page)
    def openBai18Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai18_Page)
    def openBai19Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai19_Page)
    def openBai20Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai20_Page)
    def openBai21Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai21_Page)
    def openBai22Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai22_Page)
    def openBai23Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai23_Page)
    def openBai24Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai24_Page)
    def openBai25Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai25_Page)
    def openBai26Van(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.VanBai26_Page)

    def pressed_Equal(self):
        tmp = self.cal.label.text()
        try:
            result = eval(tmp)
            self.cal.label.setText(str(round((result),5)))
        except:
            self.cal.label.setText('MATH ERROR')
    def pressed_Change(self):
        tmp = self.cal.label.text()
        if tmp[0] == '-':
            self.cal.label.setText(tmp.replace("-", "",1))
        else:
            self.cal.label.setText('-' + tmp)
    def pressed_del(self):
        tmp = self.cal.label.text()
        tmp = tmp[:-1]
        self.cal.label.setText(tmp)
    def pressed_it(self, pressed):
        if pressed == "AC":
            self.cal.label.setText("0")
        else:
            if self.cal.label.text() == "0":
                self.cal.label.setText("")
            self.cal.label.setText(f'{self.cal.label.text()}{pressed}')
    def KTGKI_GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Question1_KTGKI_GDCD)
        Temp = self.uic.Name.text()
        self.uic.Name_GDCD1.setText(str(Temp))


    def Question2_KTGKI_GDCD_Page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Question2_KTGKI_GDCD)
        Temp = self.uic.Name.text()
        self.uic.Name_GDCD1_2.setText(str(Temp))
        if self.uic.C_Button_GDCD1.isChecked():
            self.score = self.score + 1

    def Question3_KTGKI_GDCD_Page(self):
        print(self.score)
        self.uic.stackedWidget.setCurrentWidget(self.uic.Question3_KTGKI_GDCD)
        Temp = self.uic.Name.text()
        self.uic.Name_GDCD1_3.setText(str(Temp))
        if self.uic.A_Button_GDCD1_2.isChecked() == True:
            self.score = self.score + 1

    def Question4_KTGKI_GDCD_Page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Question4_KTGKI_GDCD)
        Temp = self.uic.Name.text()
        self.uic.Name_GDCD1_4.setText(str(Temp))
        if self.uic.A_Button_GDCD1_3.isChecked():
            self.score = self.score + 1

    def Question5_KTGKI_GDCD_Page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Question5_KTGKI_GDCD)
        Temp = self.uic.Name.text()
        self.uic.Name_GDCD1_5.setText(str(Temp))
        if self.uic.B_Button_GDCD1_4.isChecked():
            self.score = self.score + 1

    def Question6_KTGKI_GDCD_Page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Question6_KTGKI_GDCD)
        Temp = self.uic.Name.text()
        self.uic.Name_GDCD1_6.setText(str(Temp))
        if self.uic.D_Button_GDCD1_5.isChecked():
            self.score = self.score + 1

    def Question7_KTGKI_GDCD_Page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Question7_KTGKI_GDCD)
        Temp = self.uic.Name.text()
        self.uic.Name_GDCD1_7.setText(str(Temp))
        if self.uic.B_Button_GDCD1_6.isChecked():
            self.score = self.score + 1

    def Question8_KTGKI_GDCD_Page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Question8_KTGKI_GDCD)
        Temp = self.uic.Name.text()
        self.uic.Name_GDCD1_8.setText(str(Temp))
        if self.uic.D_Button_GDCD1_7.isChecked():
            self.score = self.score + 1

    def Question9_KTGKI_GDCD_Page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Question9_KTGKI_GDCD)
        Temp = self.uic.Name.text()
        self.uic.Name_GDCD1_9.setText(str(Temp))
        if self.uic.A_Button_GDCD1_8.isChecked():
            self.score = self.score + 1

    def Question10_KTGKI_GDCD_Page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Question10_KTGKI_GDCD)
        Temp = self.uic.Name.text()
        self.uic.Name_GDCD1_10.setText(str(Temp))
        if self.uic.B_Button_GDCD1_9.isChecked():
            self.score = self.score + 1

    def timer_start2(self):
        self.uic.Time_GDCD1.setText(str("00:05:00"))
        self.uic.Time_GDCD1.setAlignment(Qt.AlignHCenter)
        data2 = str("00:05:00")
        self.list2 = data2.split(":")
        second2 = int(self.list2[2])
        minute2 = int(self.list2[1])
        hour2 = int(self.list2[0])

        if second2 > 0 or minute2 > 0 or hour2 > 0:
            self.total_seconds2 = hour2 * 3600 + minute2 * 60 + second2
            self.my_qtimer.timeout.connect(self.timer_calculate2)
            self.my_qtimer.start(1000)

    def timer_calculate2(self):
        self.total_seconds2 -= 1
        self.hours2 = self.total_seconds2 // 3600
        total_seconds_for_minutes_and_seconds2 = self.total_seconds2 - (self.hours2 * 3600)
        self.minutes2 = total_seconds_for_minutes_and_seconds2 // 60
        self.seconds2 = total_seconds_for_minutes_and_seconds2 - (self.minutes2 * 60)
        if self.total_seconds2 <= 0:
            self.my_qtimer.disconnect()
            #playsound('Checked.mp3')
            QMessageBox.information(self, "Hết thời gian rồi :(", "Hãy nhấn OK để quay về")
            self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
        self.update_timer2()

    def update_timer2(self):
        # Cập nhật lại giá trị thời gian
        self.uic.Time_GDCD1.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours2),
                                                                  int(self.minutes2),
                                                                  int(self.seconds2)))
        self.uic.Time_GDCD1.setAlignment(Qt.AlignHCenter)

    def timer_start3(self):
        Temp = self.uic.Time_GDCD1.text()
        self.uic.Time_GDCD1_2.setText(str(Temp))
        self.uic.Time_GDCD1_2.setAlignment(Qt.AlignHCenter)
        data3 = str(Temp)
        self.list3 = data3.split(":")
        second3 = int(self.list3[2])
        minute3 = int(self.list3[1])
        hour3 = int(self.list3[0])

        if second3 > 0 or minute3 > 0 or hour3 > 0:
            self.total_seconds3 = hour3 * 3600 + minute3 * 60 + second3
            self.my_qtimer.timeout.connect(self.timer_calculate3)
            self.my_qtimer.start(1000)

    def timer_calculate3(self):
        self.total_seconds3 -= 1
        self.hours3 = self.total_seconds3 // 3600
        total_seconds_for_minutes_and_seconds3 = self.total_seconds3 - (self.hours3 * 3600)
        self.minutes3 = total_seconds_for_minutes_and_seconds3 // 60
        self.seconds3 = total_seconds_for_minutes_and_seconds3 - (self.minutes3 * 60)
        if self.total_seconds3 <= 0:
            self.my_qtimer.disconnect()
            #playsound('Checked.mp3')
            QMessageBox.information(self, "Hết thời gian rồi :(", "Hãy nhấn OK để quay về")
            self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
        self.update_timer3()

    def update_timer3(self):
        # Cập nhật lại giá trị thời gian
        self.uic.Time_GDCD1_2.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours3),
                                                                  int(self.minutes3),
                                                                  int(self.seconds3)))

    def timer_start4(self):
        Temp = self.uic.Time_GDCD1_2.text()
        self.uic.Time_GDCD1_3.setText(str(Temp))
        self.uic.Time_GDCD1_3.setAlignment(Qt.AlignHCenter)
        data4 = str(Temp)
        self.list4 = data4.split(":")
        second4 = int(self.list4[2])
        minute4 = int(self.list4[1])
        hour4 = int(self.list4[0])

        if second4 > 0 or minute4 > 0 or hour4 > 0:
            self.total_seconds4 = hour4 * 3600 + minute4 * 60 + second4
            self.my_qtimer.timeout.connect(self.timer_calculate4)
            self.my_qtimer.start(1000)

    def timer_calculate4(self):
        self.total_seconds4 -= 1
        self.hours4 = self.total_seconds4 // 3600
        total_seconds_for_minutes_and_seconds4 = self.total_seconds4 - (self.hours4 * 3600)
        self.minutes4 = total_seconds_for_minutes_and_seconds4 // 60
        self.seconds4 = total_seconds_for_minutes_and_seconds4 - (self.minutes4 * 60)
        if self.total_seconds4 <= 0:
            self.my_qtimer.disconnect()
            #playsound('Checked.mp3')
            QMessageBox.information(self, "Hết thời gian rồi :(", "Hãy nhấn OK để quay về")
            self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
        self.update_timer4()

    def update_timer4(self):
        # Cập nhật lại giá trị thời gian
        self.uic.Time_GDCD1_3.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours4),
                                                                  int(self.minutes4),
                                                                  int(self.seconds4)))

    def timer_start5(self):
        Temp = self.uic.Time_GDCD1_3.text()
        self.uic.Time_GDCD1_4.setText(str(Temp))
        self.uic.Time_GDCD1_4.setAlignment(Qt.AlignHCenter)
        data5 = str(Temp)
        self.list5 = data5.split(":")
        second5 = int(self.list5[2])
        minute5 = int(self.list5[1])
        hour5 = int(self.list5[0])

        if second5 > 0 or minute5 > 0 or hour5 > 0:
            self.total_seconds5 = hour5 * 3600 + minute5 * 60 + second5
            self.my_qtimer.timeout.connect(self.timer_calculate5)
            self.my_qtimer.start(1000)

    def timer_calculate5(self):
        self.total_seconds5 -= 1
        self.hours5 = self.total_seconds5 // 3600
        total_seconds_for_minutes_and_seconds5 = self.total_seconds5 - (self.hours5 * 3600)
        self.minutes5 = total_seconds_for_minutes_and_seconds5 // 60
        self.seconds5 = total_seconds_for_minutes_and_seconds5 - (self.minutes5 * 60)
        if self.total_seconds5 <= 0:
            self.my_qtimer.disconnect()
            #playsound('Checked.mp3')
            QMessageBox.information(self, "Hết thời gian rồi :(", "Hãy nhấn OK để quay về")
            self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
        self.update_timer5()

    def update_timer5(self):
        # Cập nhật lại giá trị thời gian
        self.uic.Time_GDCD1_4.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours5),
                                                                  int(self.minutes5),
                                                                  int(self.seconds5)))

    def timer_start6(self):
        Temp = self.uic.Time_GDCD1_4.text()
        self.uic.Time_GDCD1_5.setText(str(Temp))
        self.uic.Time_GDCD1_5.setAlignment(Qt.AlignHCenter)
        data6 = str(Temp)
        self.list6 = data6.split(":")
        second6 = int(self.list6[2])
        minute6 = int(self.list6[1])
        hour6 = int(self.list6[0])

        if second6 > 0 or minute6 > 0 or hour6 > 0:
            self.total_seconds6 = hour6 * 3600 + minute6 * 60 + second6
            self.my_qtimer.timeout.connect(self.timer_calculate6)
            self.my_qtimer.start(1000)

    def timer_calculate6(self):
        self.total_seconds6 -= 1
        self.hours6 = self.total_seconds6 // 3600
        total_seconds_for_minutes_and_seconds6 = self.total_seconds6 - (self.hours6 * 3600)
        self.minutes6 = total_seconds_for_minutes_and_seconds6 // 60
        self.seconds6 = total_seconds_for_minutes_and_seconds6 - (self.minutes6 * 60)
        if self.total_seconds6 <= 0:
            self.my_qtimer.disconnect()
            #playsound('Checked.mp3')
            QMessageBox.information(self, "Hết thời gian rồi :(", "Hãy nhấn OK để quay về")
            self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
        self.update_timer6()

    def update_timer6(self):
        # Cập nhật lại giá trị thời gian
        self.uic.Time_GDCD1_5.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours6),
                                                                  int(self.minutes6),
                                                                  int(self.seconds6)))

    def timer_start7(self):
        Temp = self.uic.Time_GDCD1_5.text()
        self.uic.Time_GDCD1_6.setText(str(Temp))
        self.uic.Time_GDCD1_6.setAlignment(Qt.AlignHCenter)
        data7 = str(Temp)
        self.list7 = data7.split(":")
        second7 = int(self.list7[2])
        minute7 = int(self.list7[1])
        hour7 = int(self.list7[0])

        if second7 > 0 or minute7 > 0 or hour7 > 0:
            self.total_seconds7 = hour7 * 3600 + minute7 * 60 + second7
            self.my_qtimer.timeout.connect(self.timer_calculate7)
            self.my_qtimer.start(1000)

    def timer_calculate7(self):
        self.total_seconds7 -= 1
        self.hours7 = self.total_seconds7 // 3600
        total_seconds_for_minutes_and_seconds7 = self.total_seconds7 - (self.hours7 * 3600)
        self.minutes7 = total_seconds_for_minutes_and_seconds7 // 60
        self.seconds7 = total_seconds_for_minutes_and_seconds7 - (self.minutes7 * 60)
        if self.total_seconds7 <= 0:
            self.my_qtimer.disconnect()
            #playsound('Checked.mp3')
            QMessageBox.information(self, "Hết thời gian rồi :(", "Hãy nhấn OK để quay về")
            self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
        self.update_timer7()

    def update_timer7(self):
        # Cập nhật lại giá trị thời gian
        self.uic.Time_GDCD1_6.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours7),
                                                                  int(self.minutes7),
                                                                  int(self.seconds7)))

    def timer_start8(self):
        Temp = self.uic.Time_GDCD1_6.text()
        self.uic.Time_GDCD1_7.setText(str(Temp))
        self.uic.Time_GDCD1_7.setAlignment(Qt.AlignHCenter)
        data8 = str(Temp)
        self.list8 = data8.split(":")
        second8 = int(self.list8[2])
        minute8 = int(self.list8[1])
        hour8 = int(self.list8[0])

        if second8 > 0 or minute8 > 0 or hour8 > 0:
            self.total_seconds8 = hour8 * 3600 + minute8 * 60 + second8
            self.my_qtimer.timeout.connect(self.timer_calculate8)
            self.my_qtimer.start(1000)

    def timer_calculate8(self):
        self.total_seconds8 -= 1
        self.hours8 = self.total_seconds8 // 3600
        total_seconds_for_minutes_and_seconds8 = self.total_seconds8 - (self.hours8 * 3600)
        self.minutes8 = total_seconds_for_minutes_and_seconds8 // 60
        self.seconds8 = total_seconds_for_minutes_and_seconds8 - (self.minutes8 * 60)
        if self.total_seconds8 <= 0:
            self.my_qtimer.disconnect()
            #playsound('Checked.mp3')
            QMessageBox.information(self, "Hết thời gian rồi :(", "Hãy nhấn OK để quay về")
            self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
        self.update_timer8()

    def update_timer8(self):
        # Cập nhật lại giá trị thời gian
        self.uic.Time_GDCD1_7.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours8),
                                                                  int(self.minutes8),
                                                                  int(self.seconds8)))

    def timer_start9(self):
        Temp = self.uic.Time_GDCD1_7.text()
        self.uic.Time_GDCD1_8.setText(str(Temp))
        self.uic.Time_GDCD1_8.setAlignment(Qt.AlignHCenter)
        data9 = str(Temp)
        self.list9 = data9.split(":")
        second9 = int(self.list9[2])
        minute9 = int(self.list9[1])
        hour9 = int(self.list9[0])

        if second9 > 0 or minute9 > 0 or hour9 > 0:
            self.total_seconds9 = hour9 * 3600 + minute9 * 60 + second9
            self.my_qtimer.timeout.connect(self.timer_calculate9)
            self.my_qtimer.start(1000)

    def timer_calculate9(self):
        self.total_seconds9 -= 1
        self.hours9 = self.total_seconds9 // 3600
        total_seconds_for_minutes_and_seconds9 = self.total_seconds9 - (self.hours9 * 3600)
        self.minutes9 = total_seconds_for_minutes_and_seconds9 // 60
        self.seconds9 = total_seconds_for_minutes_and_seconds9 - (self.minutes9 * 60)
        if self.total_seconds9 <= 0:
            self.my_qtimer.disconnect()
            #playsound('Checked.mp3')
            QMessageBox.information(self, "Hết thời gian rồi :(", "Hãy nhấn OK để quay về")
            self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
        self.update_timer9()

    def update_timer9(self):
        # Cập nhật lại giá trị thời gian
        self.uic.Time_GDCD1_8.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours9),
                                                                  int(self.minutes9),
                                                                  int(self.seconds9)))

    def timer_start10(self):
        Temp = self.uic.Time_GDCD1_8.text()
        self.uic.Time_GDCD1_9.setText(str(Temp))
        self.uic.Time_GDCD1_9.setAlignment(Qt.AlignHCenter)
        data10 = str(Temp)
        self.list10 = data10.split(":")
        second10 = int(self.list10[2])
        minute10 = int(self.list10[1])
        hour10 = int(self.list10[0])

        if second10 > 0 or minute10 > 0 or hour10 > 0:
            self.total_seconds10 = hour10 * 3600 + minute10 * 60 + second10
            self.my_qtimer.timeout.connect(self.timer_calculate10)
            self.my_qtimer.start(1000)

    def timer_calculate10(self):
        self.total_seconds10 -= 1
        self.hours10 = self.total_seconds10 // 3600
        total_seconds_for_minutes_and_seconds10 = self.total_seconds10 - (self.hours10 * 3600)
        self.minutes10 = total_seconds_for_minutes_and_seconds10 // 60
        self.seconds10 = total_seconds_for_minutes_and_seconds10 - (self.minutes10 * 60)
        if self.total_seconds10 <= 0:
            self.my_qtimer.disconnect()
            #playsound('Checked.mp3')
            QMessageBox.information(self, "Hết thời gian rồi :(", "Hãy nhấn OK để quay về")
            self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
        self.update_timer10()

    def update_timer10(self):
        # Cập nhật lại giá trị thời gian
        self.uic.Time_GDCD1_9.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours10),
                                                                    int(self.minutes10),
                                                                    int(self.seconds10)))

    def timer_start11(self):
        Temp = self.uic.Time_GDCD1_9.text()
        self.uic.Time_GDCD1_10.setText(str(Temp))
        self.uic.Time_GDCD1_10.setAlignment(Qt.AlignHCenter)
        data11 = str(Temp)
        self.list11 = data11.split(":")
        second11 = int(self.list11[2])
        minute11 = int(self.list11[1])
        hour11 = int(self.list11[0])

        if second11 > 0 or minute11 > 0 or hour11 > 0:
            self.total_seconds11 = hour11 * 3600 + minute11 * 60 + second11
            self.my_qtimer.timeout.connect(self.timer_calculate11)
            self.my_qtimer.start(1000)

    def timer_calculate11(self):
        self.total_seconds11 -= 1
        self.hours11 = self.total_seconds11 // 3600
        total_seconds_for_minutes_and_seconds11 = self.total_seconds11 - (self.hours11 * 3600)
        self.minutes11 = total_seconds_for_minutes_and_seconds11 // 60
        self.seconds11 = total_seconds_for_minutes_and_seconds11 - (self.minutes11 * 60)
        if self.total_seconds11 <= 0:
            self.my_qtimer.disconnect()
            #playsound('Checked.mp3')
            QMessageBox.information(self, "Hết thời gian rồi :(", "Hãy nhấn OK để quay về")
            self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
        self.update_timer11()

    def update_timer11(self):
        # Cập nhật lại giá trị thời gian
        self.uic.Time_GDCD1_10.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours11),
                                                                    int(self.minutes11),
                                                                    int(self.seconds11)))


    def openResult_Page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Result_Page)
        if self.uic.D_Button_GDCD1_10.isChecked():
            self.score = self.score + 1
            #playsound('Checked.mp3')
        Temp = self.uic.Time_GDCD1_10.text()
        self.uic.Time_Result.setText(str(Temp))
        self.uic.Time_Result.setAlignment(Qt.AlignHCenter)
        self.uic.Score_Result.setText(str(self.score))
        self.uic.Score_Result.setAlignment(Qt.AlignHCenter)
        Temp = self.uic.Name.text()
        self.uic.Name_Result.setText(str(Temp))
        self.uic.Name_Result.setAlignment(Qt.AlignHCenter)
        self.my_qtimer.disconnect()

#############################################################
    def timer_start(self):
        if self.uic.Start_Button.text() == 'BẮT ĐẦU':
            data = self.uic.textEdit.toPlainText()
            list = data.split(":")
            second = int(list[2])
            minute = int(list[1])
            hour = int(list[0])
            self.total_seconds = hour * 3600 + minute * 60 + second
            if self.total_seconds == 0:
                print("")
            else:
                self.uic.Start_Button.setText('TẠM DỪNG')
                self.startWatch = True
                data = self.uic.textEdit.toPlainText()
                list = data.split(":")
                second = int(list[2])
                minute = int(list[1])
                hour = int(list[0])

                if second > 0 or minute > 0 or hour > 0:
                    self.total_seconds = hour * 3600 + minute * 60 + second
                    self.my_qtimer.timeout.connect(self.timer_calculate)
                    self.my_qtimer.start(1000)

        else:
            self.uic.Start_Button.setText('BẮT ĐẦU')
            self.my_qtimer.disconnect()
            self.startWatch = False

    def timer_calculate(self):
        if self.startWatch:
            self.total_seconds -= 1
            self.hours = self.total_seconds // 3600
            total_seconds_for_minutes_and_seconds = self.total_seconds - (self.hours * 3600)
            self.minutes = total_seconds_for_minutes_and_seconds // 60
            self.seconds = total_seconds_for_minutes_and_seconds - (self.minutes * 60)
            if self.total_seconds <= 0:
                self.my_qtimer.disconnect()
                #playsound('Checked.mp3')

            self.update_timer()
        else:
            self.my_qtimer.disconnect()
    def update_timer(self):

        #Cập nhật lại giá trị thời gian
        self.uic.textEdit.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours),
                                                                int(self.minutes),
                                                                int(self.seconds)))
        self.uic.textEdit.setAlignment(Qt.AlignHCenter)

    def time_clear(self):
        self.startWatch = False
        if self.uic.Start_Button.text() == 'TẠM DỪNG':
            self.uic.Start_Button.setText('BẮT ĐẦU')
        self.uic.textEdit.setText("00:00:00")
        self.uic.textEdit.setAlignment(Qt.AlignHCenter)
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.total_seconds = 0
        #################################################

    def loginButton(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Menu)

  #Note
    def backLogin(self):
        msg = QMessageBox.question(self, "CẢNH BÁO", "Bạn có muốn thoát và kết thúc buổi học của mình?", QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:
            self.uic.stackedWidget.setCurrentWidget(self.uic.Login)
            if self.total_seconds > 0:
                QMessageBox.information(self,"Bạn đã kết thúc thời gian tự học mà bạn đặt ra!           ", "Thời gian còn lại: "
                                                                                    "{:02d}:{:02d}:{:02d}".format(int(self.hours),
                                                                                                            int(self.minutes),
                                                                                                            int(self.seconds)))

            self.time_clear()

    #############
    def openKTGKI_GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.KTGKI_GDCD)
    def openTracNghiemGDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiemGDCD)
    def openTracNghiemPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.TracNghiem)
    def openStudyWithMe(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_10)
    def openDaiSo_2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSo)
    def openBTDaiSo(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_6)
    def openBTHinhHoc(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_7)
    def JustForDaiSoButton(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSo)
    def openHinhHocLyThuyet_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHocLyThuyet_page)
    def openHinhHoc(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc)
    def openHinhHoc_Bai1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai1)
    def openHinhHoc_Bai2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai2)
    def openHinhHoc_Bai3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai3)
    def openHinhHoc_Bai4(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai4)
    def openHinhHoc_Bai5(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai5)
    def openHinhHoc_Bai6(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai6)
    def openHinhHoc_Bai7(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai7)
    def openHinhHoc_Bai8(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai8)
    def openHinhHoc_Bai9(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai9)
    def openHinhHoc_Bai10(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai10)
    def openHinhHoc_Bai11(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai11)
    def openHinhHoc_Bai12(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai12)
    def openHinhHoc_Bai13(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai13)
    def openHinhHoc_Bai14(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai14)
    def openHinhHoc_Bai15(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai15)
    def openHinhHoc_Bai16(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai16)
    def openHinhHoc_Bai17(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc_Bai17)

    def openBidongPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bidong_page)
    def openDaitunhanxungPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Daitunhanxung_page)
    def openCauhoiduoiPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Cauhoiduoi_page)

    def openHientaidonPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Hientaidon_page)
    def openHientaitiepdienPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Hientaitiepdien_page)
    def openHientaihoanthanhPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Hientaihoanthanh_page)
    def openQuakhudonPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Quakhudon_page)
    def openQuakhutiepdien(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Quakhutiepdien_page)
    def openQuakhuhoanthanhPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Quakhuhoanthanh_page)
    def openTuonglaidonPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Tuonglaidon_page)
    def openTuonglaitiepdienPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Tuonglaitiepdien_page)

    def openEnglishPage(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.English_page)
    def openBai1GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai1GDCD_page)
    def openBai2GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai2GDCD_page)
    def openBai3GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai3GDCD_page)
    def openBai4GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai4GDCD_page)
    def openBai5GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai5GDCD_page)
    def openBai6GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai6GDCD_page)
    def openBai7GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai7GDCD_page)
    def openBai8GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai8GDCD_page)
    def openBai9GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai9GDCD_page)
    def openBai10GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai10GDCD_page)
    def openBai11GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai11GDCD_page)
    def openBai12GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai12GDCD_page)
    def openBai13GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai13GDCD_page)
    def openBai14GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai14GDCD_page)

    def openBai15GDCD(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Bai15GDCD_page)

    def openGDCD_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.GDCD_page)
    def openDoisothapphannhiphan(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Doisothapphannhiphan)
    def openMangsongaunhien(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Mangsongaunhien)
    def openBaitoanlaybi(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Baitoanlaybi)
    def openKiemtramangchanle(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Kiemtramangchanle)
    def openBaiTapNangCaoIT_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.BaiTapNangCaoIT_page)

    def openDapanTinCoBan_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DapanTinCoBan_page)
    #Cau hoi
    def openChuong2IT_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Chuong2IT_page)
    def openChuong3IT_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Chuong3IT_page)
    def openChuong4IT_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Chuong4IT_page)
    def openChuong5IT_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Chuong5IT_page)
    def openChuong6IT_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Chuong6IT_page)
    #Dap an
    def openChuong2IT_page_3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Chuong2IT_page_3)
    def openChuong3IT_page_3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Chuong3IT_page_3)
    def openChuong4IT_page_3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Chuong4IT_page_3)
    def openChuong5IT_page_3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Chuong5IT_page_3)
    def openChuong6IT_page_3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Chuong6IT_page_3)

    def openDapanTinCoBan_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DapanTinCoBan_page)
    def openBaitapTinCoBan_page_2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.BaitapTinCoBan_page_2)
    def openBaitapTinCoBan_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.BaitapTinCoBan_page)
    def openBai1IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai1)
    def openBai2IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai2)
    def openBai3IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai3)
    def openBai4IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai4)
    def openBai5IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai5)
    def openBai6IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai6)
    def openBai7IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai7)
    def openBai8IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai8)
    def openBai9IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai9)
    def openBai10IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai10)
    def openBai11IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai11)
    def openBai12IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai12)
    def openBai13IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai13)
    def openBai14IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai14)
    def openBai15IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai15)
    def openBai16IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai16)
    def openBai17IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai17)
    def openBai18IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai18)
    def openBai19IT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITBai19)
    def openThuchanh1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITThuchanh1)
    def openThuchanh2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITThuchanh2)
    def openThuchanh3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITThuchanh3)
    def openThuchanh4(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITThuchanh4)
    def openThuchanh5(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITThuchanh5)
    def openThuchanh6(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITThuchanh6)
    def openThuchanh7(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITThuchanh7)
    def openThuchanh8(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ITThuchanh8)


    def openIT_page(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.IT_page)

    def openIT_page_2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.IT_page_2)
    def openChuongTrinhHocChinhIT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.IT_page_2)

    def CAPNHAT(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.TRANGCAPNHAT)

    #Mo Math_Page
    def openMath(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Math_page)
    #Mo Dai So
    def openDaiSo(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSo)
    #Mo hinh hoc
        self.uic.stackedWidget.setCurrentWidget(self.uic.HinhHoc)
    #Mo Ly Thuyet
    def openLyThuyetDaiSo(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.LyThuyetDaiSo)
    #Mo Bai tap
    def openBaiTapDaiSo(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.BaiTapDaiSo)

    #Mo bai 1 dai so
    def openDaiSoChuong1Bai1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai1)
    #def openBTDaiSoChuong1Bai1(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai1)

    def openDaiSoChuong2Bai1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai1C2)
    #def openBTDaiSoChuong2Bai1(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai1C2)

    def openDaiSoChuong3Bai1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai1C3)
    #def openBTDaiSoChuong3Bai1(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai1C3)

    def openDaiSoChuong4Bai1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai1C4)
    #def openBTDaiSoChuong4Bai1(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai1C4)

    def openDaiSoChuong5Bai1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai1C5)
    #def openBTDaiSoChuong5Bai1(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai1C5)

    #Mo bai 2 dai so
    def openDaiSoChuong1Bai2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai2)
    #def openBTDaiSoChuong1Bai2(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai2C1)

    def openDaiSoChuong2Bai2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai2C2)
    #def openBTDaiSoChuong2Bai2(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai2C2)

    def openDaiSoChuong3Bai2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai2C3)
    #def openBTDaiSoChuong3Bai2(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai2C3)

    def openDaiSoChuong4Bai2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai2C4)
    #def openBTDaiSoChuong4Bai2(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai2C4)

    def openDaiSoChuong5Bai2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai2C5)
    #def openBTDaiSoChuong5Bai2(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai2C5)

    #Mo bai 3 dai so
    def openDaiSoChuong1Bai3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai3)
    #def openBTDaiSoChuong1Bai3(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai3C1)

    def openDaiSoChuong2Bai3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai3C2)
    #def openBTDaiSoChuong2Bai3(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai3C2)

    def openDaiSoChuong3Bai3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai3C3)
    #def openBTDaiSoChuong3Bai3(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai3C3)

    def openDaiSoChuong4Bai3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai3C4)
    #def openBTDaiSoChuong4Bai3(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai3C4)

    def openDaiSoChuong5Bai3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai3C5)
    #def openBTDaiSoChuong5Bai3(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai3C5)

    #Mo bai 4 dai so
    def openDaiSoChuong2Bai4(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai4C2)
    def openBTDaiSoChuong2Bai4(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai4C2)

    def openDaiSoChuong3Bai4(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai4C3)
    #def openBTDaiSoChuong3Bai4(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai4C3)

    def openDaiSoChuong5Bai4(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai4C5)
    #def openBTDaiSoChuong5Bai4(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai4C5)

    # Mo bai 5 dai so
    def openDaiSoChuong2Bai5(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai5C2)
    #def openBTDaiSoChuong2Bai5(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai5C2)

    def openDaiSoChuong5Bai5(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.DaiSoBai5C5)
    #def openBTDaiSoChuong5Bai5(self):
    #    self.uic.stackedWidget.setCurrentWidget(self.uic.BTDaiSoBai5C5)

    #Tro ve MENU
    def BackToMenu(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Menu)



    #Mo page Thong Tin Ve San Pham
    def openProject(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Project_page)
    #Mo page Thoi Khoa Bieu

    #Mo page MON HOC
    def openSubject(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Subject_page)



if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
