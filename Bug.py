class Bug:
    def __init__(self, priority, severity, type, reproducible, assignee, status, reporter, title, description, sprint, product, team):
        self.priority = priority
        self.severity = severity
        self.type = type
        self.reproducible = reproducible
        self.assignee = assignee
        self.status = status
        self.reporter = reporter
        self.title = title
        self.description = description
        self.sprint = sprint
        self.product = product
        self.team = team

    def getPriority(self):
        print(self.priority)

    def setPriority(self, value):
        self.priority = value

    def getSeverity(self):
        print(self.severity)

    def setSeverity(self, value):
        self.severity = value

    def getType(self):
        print(self.type)

    def getReproducible(self):
        print(self.reproducible)

    def setReproducible(self, value):
        self.reproducible = value

    def getAssignee(self):
        print(self.assignee)

    def setAssignee(self, value):
        self.assignee = value

    def getStatus(self):
        print(self.status)

    def setStatus(self, value):
        self.status = value

    def getReporter(self):
        print(self.reporter)

    def getTitle(self):
        print(self.title)

    def getDescription(self):
        print(self.description)

    def setDescription(self, value):
        self.description = value

    def getSprint(self):
        print(self.sprint)

    def setSprint(self, value):
        self.sprint = value

    def getProduct(self):
        print(self.product)

    def getTeam(self):
        print(self.team)

UiBug = Bug('low', 'low', 'UI', True, 'Aleksey', 'In Progress', 'Hayk Sardaryan', 'This is a bug', 'This a description for this bug', 'Sprint7', 'Author', 'Pollux')

UiBug.getPriority()
UiBug.getSeverity()
UiBug.getType()
UiBug.getReproducible()
UiBug.getAssignee()
UiBug.getStatus()
UiBug.getReporter()
UiBug.getTitle()
UiBug.getDescription()
UiBug.getSprint()
UiBug.getProduct()
UiBug.getTeam()