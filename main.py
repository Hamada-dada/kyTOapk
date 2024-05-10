# Hvis der er dependencies der ikke virker, kør følgende kommandoer i terminalen:
# 1) pip install virtualenv
# 2) virtualenv py39venv
# 3) .\\py39venv\Scripts\activate ELLER .\\.venv\Scripts\activate (Hvis man hedder Sebastian) ELLER .\\venv\Scripts\activate (Hvis man hedder Mohamed)
# 4) pip install -r requirements.txt
# 5) garden install matplotlib

# Hvis der skal slettes et virtualenvironment, brug da:
# a) rm -r <environment_name>


from kivy.lang import Builder
from kivymd.app import MDApp
from ImportVitalsigns import VitalSignsData
from Patient import Patient
from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from Theme import Theme
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.properties import NumericProperty
import time
from TriageStatusController import TriageStatusController


data1 = VitalSignsData("testData/TriageOverviewTestData.csv", "testData/TriageOverviewTestDataTEMP.csv")
patient1 = Patient(data1)
patient1.calculateTriageCategory()

data1 = VitalSignsData("PilotTrial1/Subject2/PT1_TS2_REP2_ALGO.csv", "PilotTrial1/Subject2/PT1_TS2_REP2_TEMP.csv")
patient1 = Patient(data1)
patient1.calculateTriageCategory()

data1 = VitalSignsData("PilotTrial1/Subject2/PT1_TS2_REP3_ALGO.csv", "PilotTrial1/Subject2/PT1_TS2_REP3_TEMP.csv")
patient1 = Patient(data1)
patient1.calculateTriageCategory()


data1 = VitalSignsData("PilotTrial1/Subject1/PT1_TS1_REP1_ALGO.csv", "PilotTrial1/Subject1/PT1_TS1_REP1_TEMP.csv")
patient1 = Patient(data1)
patient1.calculateTriageCategory()

data1 = VitalSignsData("PilotTrial1/Subject1/PT1_TS1_REP2_ALGO.csv", "PilotTrial1/Subject1/PT1_TS1_REP2_TEMP.csv")
patient1 = Patient(data1)
patient1.calculateTriageCategory()

data1 = VitalSignsData("PilotTrial1/Subject1/PT1_TS1_REP3_ALGO.csv", "PilotTrial1/Subject1/PT1_TS1_REP3_TEMP.csv")
patient1 = Patient(data1)
patient1.calculateTriageCategory()



Window.size = 691, 922
Window.top = 100
Window.left = 50

Window.minimum_width = 553
Window.minimum_height = 738


class InfoPopup(FloatLayout, ModalView):
    pass

class PatientOverview(FloatLayout, ModalView):
    graphAdded = False  # Initialize the class attribute
    patientId = NumericProperty() # This seems to be the default value --> graph is created with this value before __init__ is called for some reason

    def __init__(self, patientId, **kwargs):
        print(f"Initializing PatientOverview with patientId: {self.patientId}")
        self.patientId = patientId # 
        super().__init__(**kwargs)
        
        print(f"After initialization, patientId: {self.patientId}")

    

    
    

class App(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.colors = Theme.colors
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "200"
        self.theme_cls.accent_palette = "Red"
        # Patient1.calculateTriageCategory()
        self.screen = Builder.load_file("design.kv")
        print(len(Patient.allPatients))

        self.patientOverviews = []
        for i in range (int(len(Patient.allPatients)/2)+1): # (foo/2)+1 is a workaround to create the correct number of patientOverviews
            self.patientOverviews.append(PatientOverview(patientId=Patient.allPatients[i].arrayIndex))
        TriageStatusController.start = time.time()



    def build(self):
        self.theme_cls.material_style = "M3"
        # Clock.schedule_interval(lambda dt: TriageStatusController.passCorrectData(1), 1)
        return self.screen
    


    def on_start(self):
        pass

App().run()
