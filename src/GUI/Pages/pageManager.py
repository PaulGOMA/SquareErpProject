import sys
sys.path.append("..")

from PySide6.QtWidgets import QStackedLayout, QBoxLayout

from GUI.Components.widgets import displayPageInMaintenance, createEmptypageWithButton, \
    noTaskPage
from Assets import pictures

def stackPage(layout: QBoxLayout) -> QStackedLayout:
    stack = QStackedLayout()

    dashboardPage = displayPageInMaintenance(title="Dashboard")
    reportPage = createEmptypageWithButton(title="Rapport", imagePath=":/Pictures/no_report.png", \
                                            textButton="Nouveau rapport ", firstText="Aucun rapport ou document trouvé", \
                                                secondText="Créer un nouveau rapport")
    trackingPage = noTaskPage()
    locationPage = createEmptypageWithButton(title="Sites d’inspections", imagePath=":/Pictures/no_location.png", \
                                            textButton="Nouveau site ", firstText="La liste des sites est vide",\
                                                secondText="Créer un nouveau site")
    graphPage = displayPageInMaintenance("Graphes et analyses")
    messagePage = createEmptypageWithButton(title="Messages", imagePath=":/Pictures/empty_message.png",\
                                            textButton="Nouveau message ", firstText="Aucun méssage en vu",\
                                                secondText="Démarrer une nouvelle conversation")
    adminPage = displayPageInMaintenance(title="Administration")

    stack.insertWidget(0, dashboardPage)
    stack.insertWidget(1, reportPage)
    stack.insertWidget(2, trackingPage)
    stack.insertWidget(3, locationPage)
    stack.insertWidget(4, graphPage)
    stack.insertWidget(5, messagePage)
    stack.insertWidget(6, adminPage)

    layout.addLayout(stack)

    return stack