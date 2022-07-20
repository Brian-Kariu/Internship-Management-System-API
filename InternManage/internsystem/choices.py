class Specialization:
    ENGINEER = 'engineer'
    HR = 'hr'

    CHOICES = [
        (ENGINEER, "Engineer"),
        (HR, "Hr")
    ]


class Organization:
    SCHOOL = 'school'
    COMPANY = 'company'

    CHOICES = [
        (SCHOOL, "School"),
        (COMPANY, "Company")
    ]


class Workplace:
    ONSITE = 'onsite'
    WFH = 'wfh'
    HYBRID = 'hybrid'

    CHOICES = [
        (ONSITE, "Onsite"),
        (WFH, "Wfh"),
        (HYBRID, "Hybrid")
    ]


class Employment_Type:
    FULL_TIME = 'full_time'
    PART_TIME = 'part_time'
    CONTRACT = 'contract'

    CHOICES = [
        (FULL_TIME, "Full_time"),
        (PART_TIME, "Part_time"),
        (CONTRACT, "Contract")
    ]
