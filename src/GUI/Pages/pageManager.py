import sys
sys.path.append("..")

from PySide6.QtWidgets import QStackedLayout, QBoxLayout

from GUI.Components.widgets import EmptyPage
from Assets import pictures


class PagerManager(QStackedLayout):
    """
    # This class is used to manage the application's page display.
    """

    def __init__(self, Layout: QBoxLayout):
        super().__init__()

        self.dashboardPage = EmptyPage("Dashboard", ":/Pictures/maintenance.png", "Section en cours de création")
        self.reportPage = EmptyPage("Rapport", ":/Pictures/no_report.png", "Aucun rapport ou document trouvé").emptyPageWithButton("Nouveau rapport", "Créer un nouveau site")
        self.trackingPage = EmptyPage("Suivi des missions et interventions", ":/Pictures/no_task.png", "Aucune mission en vue")
        self.locationPage = EmptyPage("Sites d'inspections", ":/Pictures/no_location.png", "La liste des sites est vide").emptyPageWithButton("Nouveau site", "Créer un nouveau site")
        self.graphPage = EmptyPage("Graphes et analyses", ":/Pictures/maintenance.png", "Section en cours de création")
        self.messagePage = EmptyPage("Messages", ":/Pictures/empty_message.png", "Aucun méssage en vu").emptyPageWithButton("Nouveau message ", "Démarrer une nouvelle conversation")
        self.adminPage = EmptyPage("Administration", ":/Pictures/maintenance.png", "Section en cours de création")

        self.insertWidget(0, self.dashboardPage)
        self.insertWidget(1, self.reportPage)
        self.insertWidget(2, self.trackingPage)
        self.insertWidget(3, self.locationPage)
        self.insertWidget(4, self.graphPage)
        self.insertWidget(5, self.messagePage)
        self.insertWidget(6, self.adminPage)

        Layout.addLayout(self)
