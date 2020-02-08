from django.core.management.base import BaseCommand
from articles.models import Category

class Command(BaseCommand):
    help = 'Populates database with new articles'

    def handle(self, *args, **kwargs):
        self.seedDatabase(self.iab)
        self.seedDatabase(self.iptc)
    

    def seedDatabase(self,dataset):
        for data in dataset:
            tax_id = data['taxonomy']+data['id']
            Category.objects.get_or_create(
                name=data['label'],
                taxonomy_id=tax_id
            )



    iptc = [{
    "id": "12009012",
    "taxonomy": "iptc-subjectcode",
    "label": "orthodoxy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "16006000",
    "taxonomy": "iptc-subjectcode",
    "label": "massacre",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "15010001",
    "taxonomy": "iptc-subjectcode",
    "label": "8 ball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010000"
    }]
    }, {
    "id": "11000000",
    "taxonomy": "iptc-subjectcode",
    "label": "politics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "15008002",
    "taxonomy": "iptc-subjectcode",
    "label": "professional - Women general",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008000"
    }]
    }, {
    "id": "15056011",
    "taxonomy": "iptc-subjectcode",
    "label": "st 3000m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "15043009",
    "taxonomy": "iptc-subjectcode",
    "label": "30km free style",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "16009003",
    "taxonomy": "iptc-subjectcode",
    "label": "prisoners and detainees",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16009003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16009000"
    }]
    }, {
    "id": "04008016",
    "taxonomy": "iptc-subjectcode",
    "label": "inflation and deflation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15037000",
    "taxonomy": "iptc-subjectcode",
    "label": "marathon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15037000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "03010004",
    "taxonomy": "iptc-subjectcode",
    "label": "maritime accident",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03010004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03010000"
    }]
    }, {
    "id": "04013000",
    "taxonomy": "iptc-subjectcode",
    "label": "process industry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "15019019",
    "taxonomy": "iptc-subjectcode",
    "label": "trial",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019019"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15075000",
    "taxonomy": "iptc-subjectcode",
    "label": "mini golf sport",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15075000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15041005",
    "taxonomy": "iptc-subjectcode",
    "label": "moto-cross",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "04010006",
    "taxonomy": "iptc-subjectcode",
    "label": "online",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "15066003",
    "taxonomy": "iptc-subjectcode",
    "label": "triathlon run",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15066003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15066000"
    }]
    }, {
    "id": "14017001",
    "taxonomy": "iptc-subjectcode",
    "label": "missing due to hostilities",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14017001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14017000"
    }]
    }, {
    "id": "05010004",
    "taxonomy": "iptc-subjectcode",
    "label": "test/examination",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05010004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05010000"
    }]
    }, {
    "id": "12009007",
    "taxonomy": "iptc-subjectcode",
    "label": "mennonite",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "11016005",
    "taxonomy": "iptc-subjectcode",
    "label": "indigenous people",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016000"
    }]
    }, {
    "id": "08005004",
    "taxonomy": "iptc-subjectcode",
    "label": "estate bestowal",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005000"
    }]
    }, {
    "id": "04006001",
    "taxonomy": "iptc-subjectcode",
    "label": "accountancy and auditing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "06003000",
    "taxonomy": "iptc-subjectcode",
    "label": "energy saving",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "08003003",
    "taxonomy": "iptc-subjectcode",
    "label": "accomplishment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003000"
    }]
    }, {
    "id": "15050013",
    "taxonomy": "iptc-subjectcode",
    "label": "monohull",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "15097000",
    "taxonomy": "iptc-subjectcode",
    "label": "kabaddi",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15097000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "17002000",
    "taxonomy": "iptc-subjectcode",
    "label": "global change",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17000000"
    }]
    }, {
    "id": "03008000",
    "taxonomy": "iptc-subjectcode",
    "label": "nuclear accident",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "06010000",
    "taxonomy": "iptc-subjectcode",
    "label": "water",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "04016045",
    "taxonomy": "iptc-subjectcode",
    "label": "sales",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016045"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15094000",
    "taxonomy": "iptc-subjectcode",
    "label": "jukendo",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15094000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15028000",
    "taxonomy": "iptc-subjectcode",
    "label": "gymnastics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04003008",
    "taxonomy": "iptc-subjectcode",
    "label": "security",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003000"
    }]
    }, {
    "id": "15051008",
    "taxonomy": "iptc-subjectcode",
    "label": "50 m free rifle 3x40",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "04004002",
    "taxonomy": "iptc-subjectcode",
    "label": "house building",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004000"
    }]
    }, {
    "id": "15073039",
    "taxonomy": "iptc-subjectcode",
    "label": "international tournament",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073039"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15056000",
    "taxonomy": "iptc-subjectcode",
    "label": "speed skating",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04016056",
    "taxonomy": "iptc-subjectcode",
    "label": "purchase",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016056"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "10017000",
    "taxonomy": "iptc-subjectcode",
    "label": "consumer issue",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10017000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "10001003",
    "taxonomy": "iptc-subjectcode",
    "label": "bridge",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10001003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10001000"
    }]
    }, {
    "id": "04014005",
    "taxonomy": "iptc-subjectcode",
    "label": "tour operator",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014000"
    }]
    }, {
    "id": "15071002",
    "taxonomy": "iptc-subjectcode",
    "label": "lake",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15071002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15071000"
    }]
    }, {
    "id": "06002002",
    "taxonomy": "iptc-subjectcode",
    "label": "ecosystem",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06002002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06002000"
    }]
    }, {
    "id": "11003008",
    "taxonomy": "iptc-subjectcode",
    "label": "poll",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }]
    }, {
    "id": "04016023",
    "taxonomy": "iptc-subjectcode",
    "label": "joint venture",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016023"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "04019000",
    "taxonomy": "iptc-subjectcode",
    "label": "finance (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04019000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "15014021",
    "taxonomy": "iptc-subjectcode",
    "label": "WBC",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014021"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "02001007",
    "taxonomy": "iptc-subjectcode",
    "label": "kidnapping",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }]
    }, {
    "id": "14010000",
    "taxonomy": "iptc-subjectcode",
    "label": "minority group",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15070007",
    "taxonomy": "iptc-subjectcode",
    "label": "over 75 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "07007001",
    "taxonomy": "iptc-subjectcode",
    "label": "herbal",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07007001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07007000"
    }]
    }, {
    "id": "04009004",
    "taxonomy": "iptc-subjectcode",
    "label": "soft commodity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04009004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04009000"
    }]
    }, {
    "id": "04007009",
    "taxonomy": "iptc-subjectcode",
    "label": "electronic commerce",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "15101000",
    "taxonomy": "iptc-subjectcode",
    "label": "bodybuilding",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15101000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15005002",
    "taxonomy": "iptc-subjectcode",
    "label": "200 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "04005000",
    "taxonomy": "iptc-subjectcode",
    "label": "energy and resource",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "11003005",
    "taxonomy": "iptc-subjectcode",
    "label": "regional elections",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }]
    }, {
    "id": "14006000",
    "taxonomy": "iptc-subjectcode",
    "label": "family",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "13003000",
    "taxonomy": "iptc-subjectcode",
    "label": "human science",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "11024001",
    "taxonomy": "iptc-subjectcode",
    "label": "political systems",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11024001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11024000"
    }]
    }, {
    "id": "15034002",
    "taxonomy": "iptc-subjectcode",
    "label": "formal exercise-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15034002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15034000"
    }]
    }, {
    "id": "14005001",
    "taxonomy": "iptc-subjectcode",
    "label": "suicide",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14005001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14005000"
    }]
    }, {
    "id": "15050002",
    "taxonomy": "iptc-subjectcode",
    "label": "soling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "15007005",
    "taxonomy": "iptc-subjectcode",
    "label": "Major League Baseball Playoffs",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007000"
    }]
    }, {
    "id": "11005001",
    "taxonomy": "iptc-subjectcode",
    "label": "economic sanction",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11005001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11005000"
    }]
    }, {
    "id": "14001000",
    "taxonomy": "iptc-subjectcode",
    "label": "addiction",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15064000",
    "taxonomy": "iptc-subjectcode",
    "label": "Taekwon-Do",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "06004000",
    "taxonomy": "iptc-subjectcode",
    "label": "environmental politics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "04007002",
    "taxonomy": "iptc-subjectcode",
    "label": "department store",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "01012000",
    "taxonomy": "iptc-subjectcode",
    "label": "painting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15007001",
    "taxonomy": "iptc-subjectcode",
    "label": "Major League Baseball (North American Professional) - American League",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007000"
    }]
    }, {
    "id": "11006001",
    "taxonomy": "iptc-subjectcode",
    "label": "civil and public service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "04006012",
    "taxonomy": "iptc-subjectcode",
    "label": "shipping service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15014022",
    "taxonomy": "iptc-subjectcode",
    "label": "WBO",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014022"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "01011000",
    "taxonomy": "iptc-subjectcode",
    "label": "music",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "04016007",
    "taxonomy": "iptc-subjectcode",
    "label": "bankruptcy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "05010001",
    "taxonomy": "iptc-subjectcode",
    "label": "students",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05010001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05010000"
    }]
    }, {
    "id": "08000000",
    "taxonomy": "iptc-subjectcode",
    "label": "human interest",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08000000"
    }]
    }, {
    "id": "13000000",
    "taxonomy": "iptc-subjectcode",
    "label": "science and technology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "09002000",
    "taxonomy": "iptc-subjectcode",
    "label": "collective contract",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "15073028",
    "taxonomy": "iptc-subjectcode",
    "label": "continental championship 1st level",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073028"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "04008013",
    "taxonomy": "iptc-subjectcode",
    "label": "economic organization",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15073043",
    "taxonomy": "iptc-subjectcode",
    "label": "friendly competition",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073043"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "01013000",
    "taxonomy": "iptc-subjectcode",
    "label": "photography",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15089000",
    "taxonomy": "iptc-subjectcode",
    "label": "inline skating",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15089000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "11006012",
    "taxonomy": "iptc-subjectcode",
    "label": "nationalisation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "04014001",
    "taxonomy": "iptc-subjectcode",
    "label": "casino and gambling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014000"
    }]
    }, {
    "id": "15078000",
    "taxonomy": "iptc-subjectcode",
    "label": "floorball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15078000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15011001",
    "taxonomy": "iptc-subjectcode",
    "label": "two-man sled",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15011001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15011000"
    }]
    }, {
    "id": "15057000",
    "taxonomy": "iptc-subjectcode",
    "label": "speedway",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15057000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15058004",
    "taxonomy": "iptc-subjectcode",
    "label": "national federation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058000"
    }]
    }, {
    "id": "03010000",
    "taxonomy": "iptc-subjectcode",
    "label": "transport accident",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "11014000",
    "taxonomy": "iptc-subjectcode",
    "label": "treaty and international organisation-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "04005011",
    "taxonomy": "iptc-subjectcode",
    "label": "natural gas",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "15051002",
    "taxonomy": "iptc-subjectcode",
    "label": "10 m air pistol",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "15028007",
    "taxonomy": "iptc-subjectcode",
    "label": "rings",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "15026001",
    "taxonomy": "iptc-subjectcode",
    "label": "moguls",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15026001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15026000"
    }]
    }, {
    "id": "15056007",
    "taxonomy": "iptc-subjectcode",
    "label": "Short-track",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "15030002",
    "taxonomy": "iptc-subjectcode",
    "label": "steeple chase",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15030002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15030000"
    }]
    }, {
    "id": "13011000",
    "taxonomy": "iptc-subjectcode",
    "label": "standards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "11012000",
    "taxonomy": "iptc-subjectcode",
    "label": "regional authority",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "14024004",
    "taxonomy": "iptc-subjectcode",
    "label": "adults",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024000"
    }]
    }, {
    "id": "12019000",
    "taxonomy": "iptc-subjectcode",
    "label": "sikhism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12019000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "11013001",
    "taxonomy": "iptc-subjectcode",
    "label": "public finance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11013001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11013000"
    }]
    }, {
    "id": "04007010",
    "taxonomy": "iptc-subjectcode",
    "label": "luxury good",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "15014008",
    "taxonomy": "iptc-subjectcode",
    "label": "welterweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "04008024",
    "taxonomy": "iptc-subjectcode",
    "label": "commodity markets",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008024"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "12014002",
    "taxonomy": "iptc-subjectcode",
    "label": "easter",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014000"
    }]
    }, {
    "id": "07001007",
    "taxonomy": "iptc-subjectcode",
    "label": "animal diseases",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001000"
    }]
    }, {
    "id": "01007000",
    "taxonomy": "iptc-subjectcode",
    "label": "fashion",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15064006",
    "taxonomy": "iptc-subjectcode",
    "label": "68-80 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064000"
    }]
    }, {
    "id": "02005000",
    "taxonomy": "iptc-subjectcode",
    "label": "prison",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "15016000",
    "taxonomy": "iptc-subjectcode",
    "label": "climbing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15049000",
    "taxonomy": "iptc-subjectcode",
    "label": "rugby union",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15049000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15015010",
    "taxonomy": "iptc-subjectcode",
    "label": "C4",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "15070005",
    "taxonomy": "iptc-subjectcode",
    "label": "63 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "15072003",
    "taxonomy": "iptc-subjectcode",
    "label": "over 130 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "15073023",
    "taxonomy": "iptc-subjectcode",
    "label": "interregional cup",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073023"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "12004002",
    "taxonomy": "iptc-subjectcode",
    "label": "islam-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004000"
    }]
    }, {
    "id": "04001006",
    "taxonomy": "iptc-subjectcode",
    "label": "aquaculture",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001000"
    }]
    }, {
    "id": "15005013",
    "taxonomy": "iptc-subjectcode",
    "label": "one hour",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15015009",
    "taxonomy": "iptc-subjectcode",
    "label": "C2",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "02009002",
    "taxonomy": "iptc-subjectcode",
    "label": "witness",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02009002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02009000"
    }]
    }, {
    "id": "16003003",
    "taxonomy": "iptc-subjectcode",
    "label": "political dissent",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003000"
    }]
    }, {
    "id": "17005000",
    "taxonomy": "iptc-subjectcode",
    "label": "warning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17000000"
    }]
    }, {
    "id": "12016000",
    "taxonomy": "iptc-subjectcode",
    "label": "nature religion",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15011000",
    "taxonomy": "iptc-subjectcode",
    "label": "bobsleigh",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15005009",
    "taxonomy": "iptc-subjectcode",
    "label": "3000 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15100000",
    "taxonomy": "iptc-subjectcode",
    "label": "darts",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15100000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15023001",
    "taxonomy": "iptc-subjectcode",
    "label": "epee",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15023001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15023000"
    }]
    }, {
    "id": "15062017",
    "taxonomy": "iptc-subjectcode",
    "label": "100 m butterfly",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062017"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "15031001",
    "taxonomy": "iptc-subjectcode",
    "label": "National Hockey League (North American)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15031001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15031000"
    }]
    }, {
    "id": "13006001",
    "taxonomy": "iptc-subjectcode",
    "label": "survey",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13006000"
    }]
    }, {
    "id": "15047000",
    "taxonomy": "iptc-subjectcode",
    "label": "rowing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "07011002",
    "taxonomy": "iptc-subjectcode",
    "label": "medicaid",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07011002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07011000"
    }]
    }, {
    "id": "02001000",
    "taxonomy": "iptc-subjectcode",
    "label": "crime",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "17003001",
    "taxonomy": "iptc-subjectcode",
    "label": "weather news",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17003000"
    }]
    }, {
    "id": "12002002",
    "taxonomy": "iptc-subjectcode",
    "label": "scientology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12002002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12002000"
    }]
    }, {
    "id": "11002002",
    "taxonomy": "iptc-subjectcode",
    "label": "international relations",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11002002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11002000"
    }]
    }, {
    "id": "15019008",
    "taxonomy": "iptc-subjectcode",
    "label": "500 m time trial",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15032009",
    "taxonomy": "iptc-subjectcode",
    "label": "pala-ancha",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "15077005",
    "taxonomy": "iptc-subjectcode",
    "label": "discathon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }]
    }, {
    "id": "13016000",
    "taxonomy": "iptc-subjectcode",
    "label": "electronics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "04010000",
    "taxonomy": "iptc-subjectcode",
    "label": "media",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "12009001",
    "taxonomy": "iptc-subjectcode",
    "label": "protestant",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "04006016",
    "taxonomy": "iptc-subjectcode",
    "label": "rental service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "07001000",
    "taxonomy": "iptc-subjectcode",
    "label": "disease",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "04016034",
    "taxonomy": "iptc-subjectcode",
    "label": "privatisation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016034"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "12002000",
    "taxonomy": "iptc-subjectcode",
    "label": "belief (faith)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15073034",
    "taxonomy": "iptc-subjectcode",
    "label": "national championship 4th level",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073034"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "11009000",
    "taxonomy": "iptc-subjectcode",
    "label": "parliament",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "15043015",
    "taxonomy": "iptc-subjectcode",
    "label": "5 km pursuit free style",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "15073046",
    "taxonomy": "iptc-subjectcode",
    "label": "Super Bowl",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073046"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "04011008",
    "taxonomy": "iptc-subjectcode",
    "label": "shipbuilding",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011000"
    }]
    }, {
    "id": "09004000",
    "taxonomy": "iptc-subjectcode",
    "label": "labour dispute",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "15056005",
    "taxonomy": "iptc-subjectcode",
    "label": "5000 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "15033001",
    "taxonomy": "iptc-subjectcode",
    "label": "heavyweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033000"
    }]
    }, {
    "id": "11023000",
    "taxonomy": "iptc-subjectcode",
    "label": "censorship",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11023000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "15043004",
    "taxonomy": "iptc-subjectcode",
    "label": "10 km pursuit free style",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "15007000",
    "taxonomy": "iptc-subjectcode",
    "label": "baseball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15074005",
    "taxonomy": "iptc-subjectcode",
    "label": "saddle bronc",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074000"
    }]
    }, {
    "id": "03015000",
    "taxonomy": "iptc-subjectcode",
    "label": "disaster (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "15005038",
    "taxonomy": "iptc-subjectcode",
    "label": "30 km walk",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005038"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15032011",
    "taxonomy": "iptc-subjectcode",
    "label": "pasaka",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "04016018",
    "taxonomy": "iptc-subjectcode",
    "label": "earnings",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016018"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15039000",
    "taxonomy": "iptc-subjectcode",
    "label": "motor racing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "01014000",
    "taxonomy": "iptc-subjectcode",
    "label": "radio",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "02004001",
    "taxonomy": "iptc-subjectcode",
    "label": "fine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02004001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02004000"
    }]
    }, {
    "id": "15014003",
    "taxonomy": "iptc-subjectcode",
    "label": "cruiserweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "04008005",
    "taxonomy": "iptc-subjectcode",
    "label": "emerging market",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15033006",
    "taxonomy": "iptc-subjectcode",
    "label": "lightweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033000"
    }]
    }, {
    "id": "15020000",
    "taxonomy": "iptc-subjectcode",
    "label": "dancing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15020000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15065000",
    "taxonomy": "iptc-subjectcode",
    "label": "tennis",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15065000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15015000",
    "taxonomy": "iptc-subjectcode",
    "label": "canoeing and kayaking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "07007000",
    "taxonomy": "iptc-subjectcode",
    "label": "medicine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "15073024",
    "taxonomy": "iptc-subjectcode",
    "label": "regional cup",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073024"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "05011004",
    "taxonomy": "iptc-subjectcode",
    "label": "madrasa",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05011004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05011000"
    }]
    }, {
    "id": "07018000",
    "taxonomy": "iptc-subjectcode",
    "label": "medical conditions",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07018000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "15021002",
    "taxonomy": "iptc-subjectcode",
    "label": "10 m platform synchronised",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021000"
    }]
    }, {
    "id": "04001003",
    "taxonomy": "iptc-subjectcode",
    "label": "forestry and timber",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001000"
    }]
    }, {
    "id": "15062013",
    "taxonomy": "iptc-subjectcode",
    "label": "50 m breaststroke",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "04016029",
    "taxonomy": "iptc-subjectcode",
    "label": "marketing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016029"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15028003",
    "taxonomy": "iptc-subjectcode",
    "label": "pommel horse",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "04008020",
    "taxonomy": "iptc-subjectcode",
    "label": "credit and debt",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008020"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "12025002",
    "taxonomy": "iptc-subjectcode",
    "label": "protestant convention",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12025002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12025000"
    }]
    }, {
    "id": "07011001",
    "taxonomy": "iptc-subjectcode",
    "label": "medicare",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07011001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07011000"
    }]
    }, {
    "id": "14024000",
    "taxonomy": "iptc-subjectcode",
    "label": "people",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "02002001",
    "taxonomy": "iptc-subjectcode",
    "label": "lawyer",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02002001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02002000"
    }]
    }, {
    "id": "04016004",
    "taxonomy": "iptc-subjectcode",
    "label": "antitrust issue",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "02012005",
    "taxonomy": "iptc-subjectcode",
    "label": "anti-trust crime",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012000"
    }]
    }, {
    "id": "15070012",
    "taxonomy": "iptc-subjectcode",
    "label": "85 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "15005027",
    "taxonomy": "iptc-subjectcode",
    "label": "decathlon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005027"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "12004005",
    "taxonomy": "iptc-subjectcode",
    "label": "hinduism-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004000"
    }]
    }, {
    "id": "15062024",
    "taxonomy": "iptc-subjectcode",
    "label": "short course",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062024"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "11001000",
    "taxonomy": "iptc-subjectcode",
    "label": "defence",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "07001003",
    "taxonomy": "iptc-subjectcode",
    "label": "AIDS",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001000"
    }]
    }, {
    "id": "13002000",
    "taxonomy": "iptc-subjectcode",
    "label": "engineering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "12026000",
    "taxonomy": "iptc-subjectcode",
    "label": "concordat",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12026000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15005064",
    "taxonomy": "iptc-subjectcode",
    "label": "1000 yards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005064"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15070001",
    "taxonomy": "iptc-subjectcode",
    "label": "snatch",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "06006004",
    "taxonomy": "iptc-subjectcode",
    "label": "wetlands",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006000"
    }]
    }, {
    "id": "04007005",
    "taxonomy": "iptc-subjectcode",
    "label": "retail",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "04016037",
    "taxonomy": "iptc-subjectcode",
    "label": "research and development",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016037"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "05003000",
    "taxonomy": "iptc-subjectcode",
    "label": "parent organisation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "15001002",
    "taxonomy": "iptc-subjectcode",
    "label": "sky diving",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15001002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15001000"
    }]
    }, {
    "id": "15056008",
    "taxonomy": "iptc-subjectcode",
    "label": "st 500 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "15005005",
    "taxonomy": "iptc-subjectcode",
    "label": "1000 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "04013007",
    "taxonomy": "iptc-subjectcode",
    "label": "textile and clothing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013000"
    }]
    }, {
    "id": "12004003",
    "taxonomy": "iptc-subjectcode",
    "label": "judaism-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004000"
    }]
    }, {
    "id": "15005016",
    "taxonomy": "iptc-subjectcode",
    "label": "110 m hurdles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "14003003",
    "taxonomy": "iptc-subjectcode",
    "label": "illegal immigrants",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14003003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14003000"
    }]
    }, {
    "id": "15043014",
    "taxonomy": "iptc-subjectcode",
    "label": "raid",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "04010011",
    "taxonomy": "iptc-subjectcode",
    "label": "music industry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "11006004",
    "taxonomy": "iptc-subjectcode",
    "label": "national government",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "13001001",
    "taxonomy": "iptc-subjectcode",
    "label": "physics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13001001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13001000"
    }]
    }, {
    "id": "15084000",
    "taxonomy": "iptc-subjectcode",
    "label": "Australian rules football",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15084000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04003000",
    "taxonomy": "iptc-subjectcode",
    "label": "computing and information technology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "15019004",
    "taxonomy": "iptc-subjectcode",
    "label": "sprint",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15032005",
    "taxonomy": "iptc-subjectcode",
    "label": "rebot",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "15073013",
    "taxonomy": "iptc-subjectcode",
    "label": "PanPacific Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15015008",
    "taxonomy": "iptc-subjectcode",
    "label": "C1",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "01011007",
    "taxonomy": "iptc-subjectcode",
    "label": "hip-hop",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011000"
    }]
    }, {
    "id": "15022001",
    "taxonomy": "iptc-subjectcode",
    "label": "three-day event",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15022001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15022000"
    }]
    }, {
    "id": "07017003",
    "taxonomy": "iptc-subjectcode",
    "label": "obesity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07017003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07017000"
    }]
    }, {
    "id": "04009003",
    "taxonomy": "iptc-subjectcode",
    "label": "securities",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04009003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04009000"
    }]
    }, {
    "id": "04016015",
    "taxonomy": "iptc-subjectcode",
    "label": "dividend announcement",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15005049",
    "taxonomy": "iptc-subjectcode",
    "label": "50 yard hurdles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005049"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15014014",
    "taxonomy": "iptc-subjectcode",
    "label": "bantamweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "04005009",
    "taxonomy": "iptc-subjectcode",
    "label": "natural resources (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "02006002",
    "taxonomy": "iptc-subjectcode",
    "label": "civil",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02006002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02006000"
    }]
    }, {
    "id": "08008000",
    "taxonomy": "iptc-subjectcode",
    "label": "plant",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08000000"
    }]
    }, {
    "id": "04012003",
    "taxonomy": "iptc-subjectcode",
    "label": "iron and steel",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012000"
    }]
    }, {
    "id": "04006011",
    "taxonomy": "iptc-subjectcode",
    "label": "market trend",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15073021",
    "taxonomy": "iptc-subjectcode",
    "label": "international cup",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073021"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15082001",
    "taxonomy": "iptc-subjectcode",
    "label": "sled",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15082001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15082000"
    }]
    }, {
    "id": "02001010",
    "taxonomy": "iptc-subjectcode",
    "label": "terrorism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }]
    }, {
    "id": "15003002",
    "taxonomy": "iptc-subjectcode",
    "label": "CFL",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15003002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15003000"
    }]
    }, {
    "id": "15025000",
    "taxonomy": "iptc-subjectcode",
    "label": "figure Skating",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15025000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15047005",
    "taxonomy": "iptc-subjectcode",
    "label": "coxless four",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047000"
    }]
    }, {
    "id": "09002003",
    "taxonomy": "iptc-subjectcode",
    "label": "contract issue-work rules",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09002003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09002000"
    }]
    }, {
    "id": "14008000",
    "taxonomy": "iptc-subjectcode",
    "label": "health insurance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "04005005",
    "taxonomy": "iptc-subjectcode",
    "label": "nuclear power",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "15053000",
    "taxonomy": "iptc-subjectcode",
    "label": "snow boarding",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15053000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "11021000",
    "taxonomy": "iptc-subjectcode",
    "label": "lobbying",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11021000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "02010000",
    "taxonomy": "iptc-subjectcode",
    "label": "organized crime",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "15072010",
    "taxonomy": "iptc-subjectcode",
    "label": "58 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "13010000",
    "taxonomy": "iptc-subjectcode",
    "label": "technology (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "15058000",
    "taxonomy": "iptc-subjectcode",
    "label": "sports organisations",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "12000000",
    "taxonomy": "iptc-subjectcode",
    "label": "religion and belief",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "02008000",
    "taxonomy": "iptc-subjectcode",
    "label": "trials",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "13004007",
    "taxonomy": "iptc-subjectcode",
    "label": "astronomy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004000"
    }]
    }, {
    "id": "15063000",
    "taxonomy": "iptc-subjectcode",
    "label": "table tennis",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15063000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04003005",
    "taxonomy": "iptc-subjectcode",
    "label": "software",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003000"
    }]
    }, {
    "id": "15055000",
    "taxonomy": "iptc-subjectcode",
    "label": "softball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15055000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "12023001",
    "taxonomy": "iptc-subjectcode",
    "label": "bible",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12023001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12023000"
    }]
    }, {
    "id": "15014007",
    "taxonomy": "iptc-subjectcode",
    "label": "light-middleweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "15077000",
    "taxonomy": "iptc-subjectcode",
    "label": "flying disc",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "13004004",
    "taxonomy": "iptc-subjectcode",
    "label": "botany",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004000"
    }]
    }, {
    "id": "15070013",
    "taxonomy": "iptc-subjectcode",
    "label": "94 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "15073002",
    "taxonomy": "iptc-subjectcode",
    "label": "Winter Olympics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "04010005",
    "taxonomy": "iptc-subjectcode",
    "label": "newspaper and magazine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "15009006",
    "taxonomy": "iptc-subjectcode",
    "label": "12.5 km pursuit",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009000"
    }]
    }, {
    "id": "04016026",
    "taxonomy": "iptc-subjectcode",
    "label": "licensing agreement",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016026"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "11001006",
    "taxonomy": "iptc-subjectcode",
    "label": "firearms",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001000"
    }]
    }, {
    "id": "15041010",
    "taxonomy": "iptc-subjectcode",
    "label": "125 cm3",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "15019012",
    "taxonomy": "iptc-subjectcode",
    "label": "road time trial",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15040003",
    "taxonomy": "iptc-subjectcode",
    "label": "rallycross",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15040003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15040000"
    }]
    }, {
    "id": "10004003",
    "taxonomy": "iptc-subjectcode",
    "label": "gardening",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10004003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10004000"
    }]
    }, {
    "id": "15005021",
    "taxonomy": "iptc-subjectcode",
    "label": "long jump",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005021"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "17000000",
    "taxonomy": "iptc-subjectcode",
    "label": "weather",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17000000"
    }]
    }, {
    "id": "15070002",
    "taxonomy": "iptc-subjectcode",
    "label": "clean and jerk",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "09005000",
    "taxonomy": "iptc-subjectcode",
    "label": "labour legislation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "04008032",
    "taxonomy": "iptc-subjectcode",
    "label": "trade agreements",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008032"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "04006006",
    "taxonomy": "iptc-subjectcode",
    "label": "insurance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15005061",
    "taxonomy": "iptc-subjectcode",
    "label": "600 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005061"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15015004",
    "taxonomy": "iptc-subjectcode",
    "label": "1000 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "15072006",
    "taxonomy": "iptc-subjectcode",
    "label": "85 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "09007000",
    "taxonomy": "iptc-subjectcode",
    "label": "retraining",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "05000000",
    "taxonomy": "iptc-subjectcode",
    "label": "education",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "12008000",
    "taxonomy": "iptc-subjectcode",
    "label": "philosophy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15014000",
    "taxonomy": "iptc-subjectcode",
    "label": "boxing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04013004",
    "taxonomy": "iptc-subjectcode",
    "label": "paper and packaging product",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013000"
    }]
    }, {
    "id": "15092000",
    "taxonomy": "iptc-subjectcode",
    "label": "twirling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15092000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15014010",
    "taxonomy": "iptc-subjectcode",
    "label": "lightweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "04011003",
    "taxonomy": "iptc-subjectcode",
    "label": "defence equipment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011000"
    }]
    }, {
    "id": "01008000",
    "taxonomy": "iptc-subjectcode",
    "label": "language",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "04016001",
    "taxonomy": "iptc-subjectcode",
    "label": "accounting and audit",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "10001004",
    "taxonomy": "iptc-subjectcode",
    "label": "shogi",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10001004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10001000"
    }]
    }, {
    "id": "15071001",
    "taxonomy": "iptc-subjectcode",
    "label": "ocean",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15071001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15071000"
    }]
    }, {
    "id": "15038002",
    "taxonomy": "iptc-subjectcode",
    "label": "shooting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038000"
    }]
    }, {
    "id": "16005000",
    "taxonomy": "iptc-subjectcode",
    "label": "guerrilla activity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "13003003",
    "taxonomy": "iptc-subjectcode",
    "label": "psychology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003000"
    }]
    }, {
    "id": "02012001",
    "taxonomy": "iptc-subjectcode",
    "label": "fraud",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012000"
    }]
    }, {
    "id": "12009003",
    "taxonomy": "iptc-subjectcode",
    "label": "reformed",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "04016048",
    "taxonomy": "iptc-subjectcode",
    "label": "corporate performance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016048"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15062003",
    "taxonomy": "iptc-subjectcode",
    "label": "200 m freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "15056012",
    "taxonomy": "iptc-subjectcode",
    "label": "st 3000m relay",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "15095000",
    "taxonomy": "iptc-subjectcode",
    "label": "naginata",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15095000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15027000",
    "taxonomy": "iptc-subjectcode",
    "label": "golf",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15027000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15062020",
    "taxonomy": "iptc-subjectcode",
    "label": "200 m medley",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062020"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "12007000",
    "taxonomy": "iptc-subjectcode",
    "label": "church and state relations",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "12027000",
    "taxonomy": "iptc-subjectcode",
    "label": "ecumenism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12027000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15067000",
    "taxonomy": "iptc-subjectcode",
    "label": "volleyball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15067000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15019014",
    "taxonomy": "iptc-subjectcode",
    "label": "cyclo-cross",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15039005",
    "taxonomy": "iptc-subjectcode",
    "label": "CART",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039000"
    }]
    }, {
    "id": "15087000",
    "taxonomy": "iptc-subjectcode",
    "label": "hornuss",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15087000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "11016001",
    "taxonomy": "iptc-subjectcode",
    "label": "data protection",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016000"
    }]
    }, {
    "id": "15002002",
    "taxonomy": "iptc-subjectcode",
    "label": "giant slalom",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002000"
    }]
    }, {
    "id": "15069002",
    "taxonomy": "iptc-subjectcode",
    "label": "trick",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15069002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15069000"
    }]
    }, {
    "id": "01022000",
    "taxonomy": "iptc-subjectcode",
    "label": "culture (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01022000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "12005000",
    "taxonomy": "iptc-subjectcode",
    "label": "church (organisation)-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "05005001",
    "taxonomy": "iptc-subjectcode",
    "label": "elementary schools",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05005001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05005000"
    }]
    }, {
    "id": "15051004",
    "taxonomy": "iptc-subjectcode",
    "label": "25 m rapid fire pistol",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "04004006",
    "taxonomy": "iptc-subjectcode",
    "label": "renovation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004000"
    }]
    }, {
    "id": "04016012",
    "taxonomy": "iptc-subjectcode",
    "label": "corporate profile",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15028011",
    "taxonomy": "iptc-subjectcode",
    "label": "hoop",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "15064003",
    "taxonomy": "iptc-subjectcode",
    "label": "49-57 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064000"
    }]
    }, {
    "id": "07003002",
    "taxonomy": "iptc-subjectcode",
    "label": "dietary supplements",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003000"
    }]
    }, {
    "id": "15073017",
    "taxonomy": "iptc-subjectcode",
    "label": "World games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073017"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "09015000",
    "taxonomy": "iptc-subjectcode",
    "label": "employer",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "15032001",
    "taxonomy": "iptc-subjectcode",
    "label": "fronton",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "02001003",
    "taxonomy": "iptc-subjectcode",
    "label": "theft",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }]
    }, {
    "id": "15062006",
    "taxonomy": "iptc-subjectcode",
    "label": "1500 m freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "06005002",
    "taxonomy": "iptc-subjectcode",
    "label": "water pollution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06005002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06005000"
    }]
    }, {
    "id": "05001000",
    "taxonomy": "iptc-subjectcode",
    "label": "adult education",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "15043003",
    "taxonomy": "iptc-subjectcode",
    "label": "10 km classical style",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "10001000",
    "taxonomy": "iptc-subjectcode",
    "label": "game",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "09010000",
    "taxonomy": "iptc-subjectcode",
    "label": "unions",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "08003004",
    "taxonomy": "iptc-subjectcode",
    "label": "human mishap",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003000"
    }]
    }, {
    "id": "04006013",
    "taxonomy": "iptc-subjectcode",
    "label": "personal service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15054000",
    "taxonomy": "iptc-subjectcode",
    "label": "soccer",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15054000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "09011001",
    "taxonomy": "iptc-subjectcode",
    "label": "employee benefits",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09011001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09011000"
    }]
    }, {
    "id": "15005010",
    "taxonomy": "iptc-subjectcode",
    "label": "5000 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "16010000",
    "taxonomy": "iptc-subjectcode",
    "label": "conflict (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "04003001",
    "taxonomy": "iptc-subjectcode",
    "label": "hardware",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003000"
    }]
    }, {
    "id": "15014011",
    "taxonomy": "iptc-subjectcode",
    "label": "super-featherweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "07001008",
    "taxonomy": "iptc-subjectcode",
    "label": "plant diseases",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001000"
    }]
    }, {
    "id": "15005050",
    "taxonomy": "iptc-subjectcode",
    "label": "60 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005050"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "01011003",
    "taxonomy": "iptc-subjectcode",
    "label": "jazz music",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011000"
    }]
    }, {
    "id": "11003009",
    "taxonomy": "iptc-subjectcode",
    "label": "european elections",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }]
    }, {
    "id": "15050006",
    "taxonomy": "iptc-subjectcode",
    "label": "470",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "15073032",
    "taxonomy": "iptc-subjectcode",
    "label": "national championship 2nd level",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073032"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "08004000",
    "taxonomy": "iptc-subjectcode",
    "label": "mystery",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08000000"
    }]
    }, {
    "id": "04008027",
    "taxonomy": "iptc-subjectcode",
    "label": "bonds",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008027"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "11001003",
    "taxonomy": "iptc-subjectcode",
    "label": "security measures",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001000"
    }]
    }, {
    "id": "15030004",
    "taxonomy": "iptc-subjectcode",
    "label": "cross country",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15030004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15030000"
    }]
    }, {
    "id": "04008035",
    "taxonomy": "iptc-subjectcode",
    "label": "tariff",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008035"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15017000",
    "taxonomy": "iptc-subjectcode",
    "label": "cricket",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15017000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15051009",
    "taxonomy": "iptc-subjectcode",
    "label": "50 m sport rifle 3x20",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "04015003",
    "taxonomy": "iptc-subjectcode",
    "label": "road transport",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04015003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04015000"
    }]
    }, {
    "id": "15080000",
    "taxonomy": "iptc-subjectcode",
    "label": "tug-of-war",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15080000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "01026000",
    "taxonomy": "iptc-subjectcode",
    "label": "mass media",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01026000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15009002",
    "taxonomy": "iptc-subjectcode",
    "label": "10 km",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009000"
    }]
    }, {
    "id": "15077004",
    "taxonomy": "iptc-subjectcode",
    "label": "distance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }]
    }, {
    "id": "15073006",
    "taxonomy": "iptc-subjectcode",
    "label": "Winter Goodwill Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "04002003",
    "taxonomy": "iptc-subjectcode",
    "label": "health and beauty product",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002000"
    }]
    }, {
    "id": "02001008",
    "taxonomy": "iptc-subjectcode",
    "label": "arson",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }]
    }, {
    "id": "11016002",
    "taxonomy": "iptc-subjectcode",
    "label": "housing and urban planning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016000"
    }]
    }, {
    "id": "15098000",
    "taxonomy": "iptc-subjectcode",
    "label": "sepak takraw",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15098000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15005037",
    "taxonomy": "iptc-subjectcode",
    "label": "20 km walk",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005037"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "06006007",
    "taxonomy": "iptc-subjectcode",
    "label": "oceans",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006000"
    }]
    }, {
    "id": "15024000",
    "taxonomy": "iptc-subjectcode",
    "label": "field Hockey",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15024000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "11003006",
    "taxonomy": "iptc-subjectcode",
    "label": "local elections",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }]
    }, {
    "id": "15073047",
    "taxonomy": "iptc-subjectcode",
    "label": "paralympic games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073047"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15002005",
    "taxonomy": "iptc-subjectcode",
    "label": "combined",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002000"
    }]
    }, {
    "id": "15050014",
    "taxonomy": "iptc-subjectcode",
    "label": "multihulls",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "15072002",
    "taxonomy": "iptc-subjectcode",
    "label": "greco-roman",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "15031000",
    "taxonomy": "iptc-subjectcode",
    "label": "ice hockey",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15031000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "02004000",
    "taxonomy": "iptc-subjectcode",
    "label": "punishment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "14015000",
    "taxonomy": "iptc-subjectcode",
    "label": "welfare",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "02011002",
    "taxonomy": "iptc-subjectcode",
    "label": "extradition",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02011002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02011000"
    }]
    }, {
    "id": "15038000",
    "taxonomy": "iptc-subjectcode",
    "label": "modern pentathlon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15005059",
    "taxonomy": "iptc-subjectcode",
    "label": "500 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005059"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "13001004",
    "taxonomy": "iptc-subjectcode",
    "label": "particle physics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13001004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13001000"
    }]
    }, {
    "id": "04002002",
    "taxonomy": "iptc-subjectcode",
    "label": "fertiliser",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002000"
    }]
    }, {
    "id": "04016020",
    "taxonomy": "iptc-subjectcode",
    "label": "government contract",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016020"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15041000",
    "taxonomy": "iptc-subjectcode",
    "label": "motorcycling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04014002",
    "taxonomy": "iptc-subjectcode",
    "label": "hotel and accommodation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014000"
    }]
    }, {
    "id": "15008003",
    "taxonomy": "iptc-subjectcode",
    "label": "Swiss netball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008000"
    }]
    }, {
    "id": "16005002",
    "taxonomy": "iptc-subjectcode",
    "label": "bombings",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16005002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16005000"
    }]
    }, {
    "id": "04006007",
    "taxonomy": "iptc-subjectcode",
    "label": "legal service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15070008",
    "taxonomy": "iptc-subjectcode",
    "label": "56 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "15052001",
    "taxonomy": "iptc-subjectcode",
    "label": "K90 jump",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15052001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15052000"
    }]
    }, {
    "id": "04006015",
    "taxonomy": "iptc-subjectcode",
    "label": "funeral parlour and crematorium",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "07000000",
    "taxonomy": "iptc-subjectcode",
    "label": "health",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "15010004",
    "taxonomy": "iptc-subjectcode",
    "label": "continuous-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010000"
    }]
    }, {
    "id": "13004002",
    "taxonomy": "iptc-subjectcode",
    "label": "paleontology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004000"
    }]
    }, {
    "id": "14011000",
    "taxonomy": "iptc-subjectcode",
    "label": "pornography",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15102000",
    "taxonomy": "iptc-subjectcode",
    "label": "sports disciplinary action",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15102000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15070015",
    "taxonomy": "iptc-subjectcode",
    "label": "over 105 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "04011005",
    "taxonomy": "iptc-subjectcode",
    "label": "heavy engineering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011000"
    }]
    }, {
    "id": "14017000",
    "taxonomy": "iptc-subjectcode",
    "label": "missing person",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14017000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15025003",
    "taxonomy": "iptc-subjectcode",
    "label": "ice dance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15025003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15025000"
    }]
    }, {
    "id": "13003002",
    "taxonomy": "iptc-subjectcode",
    "label": "history",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003000"
    }]
    }, {
    "id": "04008025",
    "taxonomy": "iptc-subjectcode",
    "label": "investments",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008025"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "13003001",
    "taxonomy": "iptc-subjectcode",
    "label": "social sciences",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003000"
    }]
    }, {
    "id": "15077009",
    "taxonomy": "iptc-subjectcode",
    "label": "accuracy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }]
    }, {
    "id": "15043007",
    "taxonomy": "iptc-subjectcode",
    "label": "10 km + 15 km combined",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "15074004",
    "taxonomy": "iptc-subjectcode",
    "label": "bulldogging",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074000"
    }]
    }, {
    "id": "05011000",
    "taxonomy": "iptc-subjectcode",
    "label": "religious education",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "05006000",
    "taxonomy": "iptc-subjectcode",
    "label": "teachers union",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "04007003",
    "taxonomy": "iptc-subjectcode",
    "label": "food",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "15001001",
    "taxonomy": "iptc-subjectcode",
    "label": "parachuting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15001001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15001000"
    }]
    }, {
    "id": "15050003",
    "taxonomy": "iptc-subjectcode",
    "label": "49er",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "14009000",
    "taxonomy": "iptc-subjectcode",
    "label": "homelessness",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "11009001",
    "taxonomy": "iptc-subjectcode",
    "label": "upper house",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11009001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11009000"
    }]
    }, {
    "id": "04008011",
    "taxonomy": "iptc-subjectcode",
    "label": "international (foreign) trade",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "08006001",
    "taxonomy": "iptc-subjectcode",
    "label": "record",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08006000"
    }]
    }, {
    "id": "07001004",
    "taxonomy": "iptc-subjectcode",
    "label": "cancer",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001000"
    }]
    }, {
    "id": "11006000",
    "taxonomy": "iptc-subjectcode",
    "label": "government",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "15014015",
    "taxonomy": "iptc-subjectcode",
    "label": "super-flyweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "01016000",
    "taxonomy": "iptc-subjectcode",
    "label": "television",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15006000",
    "taxonomy": "iptc-subjectcode",
    "label": "badminton",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04016030",
    "taxonomy": "iptc-subjectcode",
    "label": "new product",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016030"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15062016",
    "taxonomy": "iptc-subjectcode",
    "label": "50 m butterfly",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "05009000",
    "taxonomy": "iptc-subjectcode",
    "label": "entrance examination",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "11006011",
    "taxonomy": "iptc-subjectcode",
    "label": "privatisation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "15043011",
    "taxonomy": "iptc-subjectcode",
    "label": "4x5 km relay",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "07006002",
    "taxonomy": "iptc-subjectcode",
    "label": "health-workers union",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07006002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07006000"
    }]
    }, {
    "id": "01007001",
    "taxonomy": "iptc-subjectcode",
    "label": "jewelry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01007001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01007000"
    }]
    }, {
    "id": "04004001",
    "taxonomy": "iptc-subjectcode",
    "label": "heavy construction",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004000"
    }]
    }, {
    "id": "15050008",
    "taxonomy": "iptc-subjectcode",
    "label": "Star",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "16001000",
    "taxonomy": "iptc-subjectcode",
    "label": "act of terror",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "15073042",
    "taxonomy": "iptc-subjectcode",
    "label": "inter-clubs competition",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073042"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "12014005",
    "taxonomy": "iptc-subjectcode",
    "label": "yom kippur",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014000"
    }]
    }, {
    "id": "11010001",
    "taxonomy": "iptc-subjectcode",
    "label": "non government organizations (NGO)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11010001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11010000"
    }]
    }, {
    "id": "15073029",
    "taxonomy": "iptc-subjectcode",
    "label": "continental championship 2nd level",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073029"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15010002",
    "taxonomy": "iptc-subjectcode",
    "label": "9 ball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010000"
    }]
    }, {
    "id": "11007000",
    "taxonomy": "iptc-subjectcode",
    "label": "human rights",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "13012000",
    "taxonomy": "iptc-subjectcode",
    "label": "animal science",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "15077008",
    "taxonomy": "iptc-subjectcode",
    "label": "freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }]
    }, {
    "id": "16004000",
    "taxonomy": "iptc-subjectcode",
    "label": "coup d'etat",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "15043008",
    "taxonomy": "iptc-subjectcode",
    "label": "30 km classical style",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "04005010",
    "taxonomy": "iptc-subjectcode",
    "label": "energy (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "15005019",
    "taxonomy": "iptc-subjectcode",
    "label": "high jump",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005019"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15019001",
    "taxonomy": "iptc-subjectcode",
    "label": "track",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15015005",
    "taxonomy": "iptc-subjectcode",
    "label": "K1",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "04016014",
    "taxonomy": "iptc-subjectcode",
    "label": "defence contract",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "02001004",
    "taxonomy": "iptc-subjectcode",
    "label": "drug trafficking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }]
    }, {
    "id": "15056010",
    "taxonomy": "iptc-subjectcode",
    "label": "st 1500m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "04008014",
    "taxonomy": "iptc-subjectcode",
    "label": "consumer confidence",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "11024000",
    "taxonomy": "iptc-subjectcode",
    "label": "politics (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11024000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "04016031",
    "taxonomy": "iptc-subjectcode",
    "label": "patent, copyright and trademark",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016031"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "07015000",
    "taxonomy": "iptc-subjectcode",
    "label": "medical service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "04007008",
    "taxonomy": "iptc-subjectcode",
    "label": "beverage",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "02012000",
    "taxonomy": "iptc-subjectcode",
    "label": "corporate crime",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "12024000",
    "taxonomy": "iptc-subjectcode",
    "label": "interreligious dialogue",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12024000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15073010",
    "taxonomy": "iptc-subjectcode",
    "label": "African Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "03015001",
    "taxonomy": "iptc-subjectcode",
    "label": "natural disasters",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03015001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03015000"
    }]
    }, {
    "id": "14005000",
    "taxonomy": "iptc-subjectcode",
    "label": "euthanasia (also includes assisted suicide)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15032012",
    "taxonomy": "iptc-subjectcode",
    "label": "xare",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "04016017",
    "taxonomy": "iptc-subjectcode",
    "label": "financially distressed company",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016017"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15041012",
    "taxonomy": "iptc-subjectcode",
    "label": "500 cm3",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "11014003",
    "taxonomy": "iptc-subjectcode",
    "label": "alliances-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11014003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11014000"
    }]
    }, {
    "id": "08005001",
    "taxonomy": "iptc-subjectcode",
    "label": "ceremony",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005000"
    }]
    }, {
    "id": "07014004",
    "taxonomy": "iptc-subjectcode",
    "label": "genetics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014000"
    }]
    }, {
    "id": "15051007",
    "taxonomy": "iptc-subjectcode",
    "label": "50 m free rifle prone",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "15005008",
    "taxonomy": "iptc-subjectcode",
    "label": "2000 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15005033",
    "taxonomy": "iptc-subjectcode",
    "label": "walk 1 h",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005033"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15007002",
    "taxonomy": "iptc-subjectcode",
    "label": "Major League Baseball (North American Professional) - National League",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007000"
    }]
    }, {
    "id": "14003004",
    "taxonomy": "iptc-subjectcode",
    "label": "emigrants",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14003004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14003000"
    }]
    }, {
    "id": "15021004",
    "taxonomy": "iptc-subjectcode",
    "label": "3 m springboard synchronised",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021000"
    }]
    }, {
    "id": "06002001",
    "taxonomy": "iptc-subjectcode",
    "label": "endangered species",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06002001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06002000"
    }]
    }, {
    "id": "04016039",
    "taxonomy": "iptc-subjectcode",
    "label": "restructuring and recapitalisation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016039"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "01000000",
    "taxonomy": "iptc-subjectcode",
    "label": "arts, culture and entertainment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15033005",
    "taxonomy": "iptc-subjectcode",
    "label": "half-lightweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033000"
    }]
    }, {
    "id": "12005001",
    "taxonomy": "iptc-subjectcode",
    "label": "religious facilities-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12005001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12005000"
    }]
    }, {
    "id": "05010000",
    "taxonomy": "iptc-subjectcode",
    "label": "teaching and learning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "03016000",
    "taxonomy": "iptc-subjectcode",
    "label": "emergency planning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "15045000",
    "taxonomy": "iptc-subjectcode",
    "label": "polo",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15045000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15056004",
    "taxonomy": "iptc-subjectcode",
    "label": "3000 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "04016041",
    "taxonomy": "iptc-subjectcode",
    "label": "stock activity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016041"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "02015000",
    "taxonomy": "iptc-subjectcode",
    "label": "inquiry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "15032008",
    "taxonomy": "iptc-subjectcode",
    "label": "bare hand",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "04008019",
    "taxonomy": "iptc-subjectcode",
    "label": "budgets and budgeting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008019"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15005048",
    "taxonomy": "iptc-subjectcode",
    "label": "50 yards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005048"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "09003003",
    "taxonomy": "iptc-subjectcode",
    "label": "child labor",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09003003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09003000"
    }]
    }, {
    "id": "15028014",
    "taxonomy": "iptc-subjectcode",
    "label": "ball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "11004000",
    "taxonomy": "iptc-subjectcode",
    "label": "espionage and intelligence",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "14006006",
    "taxonomy": "iptc-subjectcode",
    "label": "courtship",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006000"
    }]
    }, {
    "id": "15041004",
    "taxonomy": "iptc-subjectcode",
    "label": "moto-ball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "15028008",
    "taxonomy": "iptc-subjectcode",
    "label": "beam",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "15073035",
    "taxonomy": "iptc-subjectcode",
    "label": "regional championship",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073035"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15051001",
    "taxonomy": "iptc-subjectcode",
    "label": "10 m air rifle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "16007000",
    "taxonomy": "iptc-subjectcode",
    "label": "riots",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "15033002",
    "taxonomy": "iptc-subjectcode",
    "label": "half-heavyweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033000"
    }]
    }, {
    "id": "04003004",
    "taxonomy": "iptc-subjectcode",
    "label": "semiconductors and active components",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003000"
    }]
    }, {
    "id": "04005006",
    "taxonomy": "iptc-subjectcode",
    "label": "electricity production and distribution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "04016052",
    "taxonomy": "iptc-subjectcode",
    "label": "stock options",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016052"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15007004",
    "taxonomy": "iptc-subjectcode",
    "label": "rubberball baseball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007000"
    }]
    }, {
    "id": "10007001",
    "taxonomy": "iptc-subjectcode",
    "label": "traffic",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10007001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10007000"
    }]
    }, {
    "id": "15013000",
    "taxonomy": "iptc-subjectcode",
    "label": "bowls and petanque",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04006000",
    "taxonomy": "iptc-subjectcode",
    "label": "financial and business service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "11005000",
    "taxonomy": "iptc-subjectcode",
    "label": "foreign aid",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "15070004",
    "taxonomy": "iptc-subjectcode",
    "label": "53 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "15090000",
    "taxonomy": "iptc-subjectcode",
    "label": "grass ski",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15090000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "03007001",
    "taxonomy": "iptc-subjectcode",
    "label": "windstorms",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03007001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03007000"
    }]
    }, {
    "id": "14025005",
    "taxonomy": "iptc-subjectcode",
    "label": "death penalty policies",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025000"
    }]
    }, {
    "id": "12012000",
    "taxonomy": "iptc-subjectcode",
    "label": "buddhism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15074000",
    "taxonomy": "iptc-subjectcode",
    "label": "rodeo",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04016006",
    "taxonomy": "iptc-subjectcode",
    "label": "analysts' comment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15047001",
    "taxonomy": "iptc-subjectcode",
    "label": "single sculls",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047000"
    }]
    }, {
    "id": "10011000",
    "taxonomy": "iptc-subjectcode",
    "label": "public holiday",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "01002000",
    "taxonomy": "iptc-subjectcode",
    "label": "architecture",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15019005",
    "taxonomy": "iptc-subjectcode",
    "label": "Keirin",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15088000",
    "taxonomy": "iptc-subjectcode",
    "label": "fist ball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15088000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "01011004",
    "taxonomy": "iptc-subjectcode",
    "label": "popular music",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011000"
    }]
    }, {
    "id": "15051012",
    "taxonomy": "iptc-subjectcode",
    "label": "skeet",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "04008004",
    "taxonomy": "iptc-subjectcode",
    "label": "economic indicator",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15016002",
    "taxonomy": "iptc-subjectcode",
    "label": "sport climbing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15016002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15016000"
    }]
    }, {
    "id": "15011002",
    "taxonomy": "iptc-subjectcode",
    "label": "four-man sled",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15011002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15011000"
    }]
    }, {
    "id": "04010001",
    "taxonomy": "iptc-subjectcode",
    "label": "advertising",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "15052003",
    "taxonomy": "iptc-subjectcode",
    "label": "K180 (flying jump)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15052003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15052000"
    }]
    }, {
    "id": "15014019",
    "taxonomy": "iptc-subjectcode",
    "label": "IBF",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014019"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "07007002",
    "taxonomy": "iptc-subjectcode",
    "label": "holistic",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07007002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07007000"
    }]
    }, {
    "id": "15004001",
    "taxonomy": "iptc-subjectcode",
    "label": "FITA / Outdoor target archery",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15004001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15004000"
    }]
    }, {
    "id": "15022000",
    "taxonomy": "iptc-subjectcode",
    "label": "equestrian",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15022000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "16009002",
    "taxonomy": "iptc-subjectcode",
    "label": "international military intervention",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16009002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16009000"
    }]
    }, {
    "id": "15058005",
    "taxonomy": "iptc-subjectcode",
    "label": "GAISF",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058000"
    }]
    }, {
    "id": "12018000",
    "taxonomy": "iptc-subjectcode",
    "label": "shintoism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12018000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15019016",
    "taxonomy": "iptc-subjectcode",
    "label": "Vtt-cross",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "04009000",
    "taxonomy": "iptc-subjectcode",
    "label": "market and exchange",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "03010001",
    "taxonomy": "iptc-subjectcode",
    "label": "road accident",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03010001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03010000"
    }]
    }, {
    "id": "04011002",
    "taxonomy": "iptc-subjectcode",
    "label": "automotive equipment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011000"
    }]
    }, {
    "id": "13023000",
    "taxonomy": "iptc-subjectcode",
    "label": "scientific institutions",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13023000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "14025004",
    "taxonomy": "iptc-subjectcode",
    "label": "social services",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025000"
    }]
    }, {
    "id": "11008000",
    "taxonomy": "iptc-subjectcode",
    "label": "local authority",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "01001000",
    "taxonomy": "iptc-subjectcode",
    "label": "archaeology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "08005005",
    "taxonomy": "iptc-subjectcode",
    "label": "memorial",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005000"
    }]
    }, {
    "id": "15073031",
    "taxonomy": "iptc-subjectcode",
    "label": "national championship 1st level",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073031"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "13004008",
    "taxonomy": "iptc-subjectcode",
    "label": "biology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004000"
    }]
    }, {
    "id": "15056003",
    "taxonomy": "iptc-subjectcode",
    "label": "1500 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "02012007",
    "taxonomy": "iptc-subjectcode",
    "label": "bribery",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012000"
    }]
    }, {
    "id": "15071000",
    "taxonomy": "iptc-subjectcode",
    "label": "windsurfing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15071000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15058001",
    "taxonomy": "iptc-subjectcode",
    "label": "IOC",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058000"
    }]
    }, {
    "id": "07013000",
    "taxonomy": "iptc-subjectcode",
    "label": "healthcare policy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "04008036",
    "taxonomy": "iptc-subjectcode",
    "label": "trade balance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008036"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15059000",
    "taxonomy": "iptc-subjectcode",
    "label": "squash",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15059000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15014004",
    "taxonomy": "iptc-subjectcode",
    "label": "light-heavyweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "15019003",
    "taxonomy": "iptc-subjectcode",
    "label": "Olympic sprint",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "14003000",
    "taxonomy": "iptc-subjectcode",
    "label": "demographics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "04013008",
    "taxonomy": "iptc-subjectcode",
    "label": "tobacco",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013000"
    }]
    }, {
    "id": "15005004",
    "taxonomy": "iptc-subjectcode",
    "label": "800 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "11002004",
    "taxonomy": "iptc-subjectcode",
    "label": "alliances",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11002004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11002000"
    }]
    }, {
    "id": "01015000",
    "taxonomy": "iptc-subjectcode",
    "label": "sculpture",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15073007",
    "taxonomy": "iptc-subjectcode",
    "label": "Summer Asian Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "16003002",
    "taxonomy": "iptc-subjectcode",
    "label": "rebellions",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003000"
    }]
    }, {
    "id": "15046000",
    "taxonomy": "iptc-subjectcode",
    "label": "power boating",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15046000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15005065",
    "taxonomy": "iptc-subjectcode",
    "label": "2 miles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005065"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15019011",
    "taxonomy": "iptc-subjectcode",
    "label": "road race",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15036002",
    "taxonomy": "iptc-subjectcode",
    "label": "doubles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15036002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15036000"
    }]
    }, {
    "id": "15069001",
    "taxonomy": "iptc-subjectcode",
    "label": "slalom",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15069001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15069000"
    }]
    }, {
    "id": "15062010",
    "taxonomy": "iptc-subjectcode",
    "label": "50 m backstroke",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "04015004",
    "taxonomy": "iptc-subjectcode",
    "label": "waterway and maritime transport",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04015004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04015000"
    }]
    }, {
    "id": "08003002",
    "taxonomy": "iptc-subjectcode",
    "label": "celebrity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003000"
    }]
    }, {
    "id": "15032004",
    "taxonomy": "iptc-subjectcode",
    "label": "trinquet",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "01010000",
    "taxonomy": "iptc-subjectcode",
    "label": "literature",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "07017002",
    "taxonomy": "iptc-subjectcode",
    "label": "eating disorder",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07017002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07017000"
    }]
    }, {
    "id": "10001001",
    "taxonomy": "iptc-subjectcode",
    "label": "Go",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10001001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10001000"
    }]
    }, {
    "id": "14026000",
    "taxonomy": "iptc-subjectcode",
    "label": "ordnance clearance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14026000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15053002",
    "taxonomy": "iptc-subjectcode",
    "label": "half-pipe",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15053002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15053000"
    }]
    }, {
    "id": "04007000",
    "taxonomy": "iptc-subjectcode",
    "label": "consumer goods",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "16010001",
    "taxonomy": "iptc-subjectcode",
    "label": "peacekeeping force",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16010001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16010000"
    }]
    }, {
    "id": "02006001",
    "taxonomy": "iptc-subjectcode",
    "label": "criminal",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02006000"
    }]
    }, {
    "id": "11003001",
    "taxonomy": "iptc-subjectcode",
    "label": "political candidates",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }]
    }, {
    "id": "04007011",
    "taxonomy": "iptc-subjectcode",
    "label": "non-durable good",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "15041008",
    "taxonomy": "iptc-subjectcode",
    "label": "endurance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "04006010",
    "taxonomy": "iptc-subjectcode",
    "label": "personal investing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15028004",
    "taxonomy": "iptc-subjectcode",
    "label": "uneven bars",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "04001002",
    "taxonomy": "iptc-subjectcode",
    "label": "fishing industry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001000"
    }]
    }, {
    "id": "04016028",
    "taxonomy": "iptc-subjectcode",
    "label": "management change",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016028"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15082002",
    "taxonomy": "iptc-subjectcode",
    "label": "oval track",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15082002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15082000"
    }]
    }, {
    "id": "07005000",
    "taxonomy": "iptc-subjectcode",
    "label": "medical research",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "04005002",
    "taxonomy": "iptc-subjectcode",
    "label": "coal",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "11003003",
    "taxonomy": "iptc-subjectcode",
    "label": "campaign finance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }]
    }, {
    "id": "12004004",
    "taxonomy": "iptc-subjectcode",
    "label": "buddhism-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004000"
    }]
    }, {
    "id": "15062002",
    "taxonomy": "iptc-subjectcode",
    "label": "100 m freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "09008000",
    "taxonomy": "iptc-subjectcode",
    "label": "strike",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "11001001",
    "taxonomy": "iptc-subjectcode",
    "label": "veterans affairs",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001000"
    }]
    }, {
    "id": "15070000",
    "taxonomy": "iptc-subjectcode",
    "label": "weightlifting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04008001",
    "taxonomy": "iptc-subjectcode",
    "label": "central bank",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "09003002",
    "taxonomy": "iptc-subjectcode",
    "label": "job layoffs",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09003002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09003000"
    }]
    }, {
    "id": "15056009",
    "taxonomy": "iptc-subjectcode",
    "label": "st 1000m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "15062021",
    "taxonomy": "iptc-subjectcode",
    "label": "400 m medley",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062021"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "12009009",
    "taxonomy": "iptc-subjectcode",
    "label": "mormon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "15064007",
    "taxonomy": "iptc-subjectcode",
    "label": "over 67 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064000"
    }]
    }, {
    "id": "15077001",
    "taxonomy": "iptc-subjectcode",
    "label": "ultimate",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }]
    }, {
    "id": "04008000",
    "taxonomy": "iptc-subjectcode",
    "label": "macro economics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "15005054",
    "taxonomy": "iptc-subjectcode",
    "label": "100 yards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005054"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "04010004",
    "taxonomy": "iptc-subjectcode",
    "label": "news agency",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "04015000",
    "taxonomy": "iptc-subjectcode",
    "label": "transport",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "14024003",
    "taxonomy": "iptc-subjectcode",
    "label": "teen-agers",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024000"
    }]
    }, {
    "id": "07003003",
    "taxonomy": "iptc-subjectcode",
    "label": "diet",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003000"
    }]
    }, {
    "id": "15005022",
    "taxonomy": "iptc-subjectcode",
    "label": "triple jump",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005022"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15022004",
    "taxonomy": "iptc-subjectcode",
    "label": "cross country",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15022004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15022000"
    }]
    }, {
    "id": "15005062",
    "taxonomy": "iptc-subjectcode",
    "label": "600 yards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005062"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15043000",
    "taxonomy": "iptc-subjectcode",
    "label": "nordic skiing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15019009",
    "taxonomy": "iptc-subjectcode",
    "label": "1 km time trial",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "12014000",
    "taxonomy": "iptc-subjectcode",
    "label": "religious festival or holiday",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15072005",
    "taxonomy": "iptc-subjectcode",
    "label": "97 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "10010000",
    "taxonomy": "iptc-subjectcode",
    "label": "leisure (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "04012002",
    "taxonomy": "iptc-subjectcode",
    "label": "gold and precious material",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012000"
    }]
    }, {
    "id": "04006020",
    "taxonomy": "iptc-subjectcode",
    "label": "auction service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006020"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15005011",
    "taxonomy": "iptc-subjectcode",
    "label": "10,000 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "07014005",
    "taxonomy": "iptc-subjectcode",
    "label": "obstetrics/gynecology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014000"
    }]
    }, {
    "id": "04016047",
    "taxonomy": "iptc-subjectcode",
    "label": "shareholders",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016047"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "10008000",
    "taxonomy": "iptc-subjectcode",
    "label": "club and association",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "15005051",
    "taxonomy": "iptc-subjectcode",
    "label": "60 m hurdles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005051"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15005000",
    "taxonomy": "iptc-subjectcode",
    "label": "athletics, track and field",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15073018",
    "taxonomy": "iptc-subjectcode",
    "label": "World Cup",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073018"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15073020",
    "taxonomy": "iptc-subjectcode",
    "label": "continental cup",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073020"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15003001",
    "taxonomy": "iptc-subjectcode",
    "label": "(US) National Football League (NFL) (North American)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15003000"
    }]
    }, {
    "id": "11018000",
    "taxonomy": "iptc-subjectcode",
    "label": "citizens initiative and recall",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11018000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "03014001",
    "taxonomy": "iptc-subjectcode",
    "label": "explosion",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03014001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03014000"
    }]
    }, {
    "id": "15005040",
    "taxonomy": "iptc-subjectcode",
    "label": "100 m hurdles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005040"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15103000",
    "taxonomy": "iptc-subjectcode",
    "label": "sports awards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15103000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "06011000",
    "taxonomy": "iptc-subjectcode",
    "label": "global warming",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "15085000",
    "taxonomy": "iptc-subjectcode",
    "label": "Canadian football",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15085000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "02009001",
    "taxonomy": "iptc-subjectcode",
    "label": "defendant",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02009001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02009000"
    }]
    }, {
    "id": "13001000",
    "taxonomy": "iptc-subjectcode",
    "label": "applied science",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "13008000",
    "taxonomy": "iptc-subjectcode",
    "label": "space programme",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "15039008",
    "taxonomy": "iptc-subjectcode",
    "label": "TRUCKI",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039000"
    }]
    }, {
    "id": "06006003",
    "taxonomy": "iptc-subjectcode",
    "label": "forests",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006000"
    }]
    }, {
    "id": "12014004",
    "taxonomy": "iptc-subjectcode",
    "label": "ramadan",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014000"
    }]
    }, {
    "id": "15010005",
    "taxonomy": "iptc-subjectcode",
    "label": "other-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010000"
    }]
    }, {
    "id": "04016036",
    "taxonomy": "iptc-subjectcode",
    "label": "rating",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016036"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15002001",
    "taxonomy": "iptc-subjectcode",
    "label": "downhill",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002000"
    }]
    }, {
    "id": "15073003",
    "taxonomy": "iptc-subjectcode",
    "label": "Summer universiade",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15070016",
    "taxonomy": "iptc-subjectcode",
    "label": "powerlifting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "15005015",
    "taxonomy": "iptc-subjectcode",
    "label": "30000",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "12013000",
    "taxonomy": "iptc-subjectcode",
    "label": "hinduism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15073036",
    "taxonomy": "iptc-subjectcode",
    "label": "Grand Prix",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073036"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15009003",
    "taxonomy": "iptc-subjectcode",
    "label": "15 km",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009000"
    }]
    }, {
    "id": "04008008",
    "taxonomy": "iptc-subjectcode",
    "label": "government debt",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "04016025",
    "taxonomy": "iptc-subjectcode",
    "label": "layoffs and downsizing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016025"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15041001",
    "taxonomy": "iptc-subjectcode",
    "label": "speed-Grand-Prix",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "06006008",
    "taxonomy": "iptc-subjectcode",
    "label": "wildlife",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006000"
    }]
    }, {
    "id": "11001009",
    "taxonomy": "iptc-subjectcode",
    "label": "nuclear weapons",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001000"
    }]
    }, {
    "id": "15040002",
    "taxonomy": "iptc-subjectcode",
    "label": "pursuit",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15040002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15040000"
    }]
    }, {
    "id": "15028010",
    "taxonomy": "iptc-subjectcode",
    "label": "clubs",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "14025003",
    "taxonomy": "iptc-subjectcode",
    "label": "discrimination",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025000"
    }]
    }, {
    "id": "04011009",
    "taxonomy": "iptc-subjectcode",
    "label": "machine manufacturing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011000"
    }]
    }, {
    "id": "13022000",
    "taxonomy": "iptc-subjectcode",
    "label": "IT/computer sciences",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13022000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "04019001",
    "taxonomy": "iptc-subjectcode",
    "label": "money and monetary policy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04019001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04019000"
    }]
    }, {
    "id": "04006019",
    "taxonomy": "iptc-subjectcode",
    "label": "personal income",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006019"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "04008033",
    "taxonomy": "iptc-subjectcode",
    "label": "trade policy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008033"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15021001",
    "taxonomy": "iptc-subjectcode",
    "label": "10 m platform",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021000"
    }]
    }, {
    "id": "06000000",
    "taxonomy": "iptc-subjectcode",
    "label": "environmental issue",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "15070011",
    "taxonomy": "iptc-subjectcode",
    "label": "77 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "16012000",
    "taxonomy": "iptc-subjectcode",
    "label": "weaponry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "15005032",
    "taxonomy": "iptc-subjectcode",
    "label": "4x1500 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005032"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "02016000",
    "taxonomy": "iptc-subjectcode",
    "label": "tribunal",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "15014001",
    "taxonomy": "iptc-subjectcode",
    "label": "super-heavyweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "15039006",
    "taxonomy": "iptc-subjectcode",
    "label": "NHRA",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039000"
    }]
    }, {
    "id": "04006003",
    "taxonomy": "iptc-subjectcode",
    "label": "consultancy service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "14018000",
    "taxonomy": "iptc-subjectcode",
    "label": "long term care",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14018000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15068000",
    "taxonomy": "iptc-subjectcode",
    "label": "water polo",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15068000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "12009004",
    "taxonomy": "iptc-subjectcode",
    "label": "anglican",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "04008021",
    "taxonomy": "iptc-subjectcode",
    "label": "loans",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008021"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "04013003",
    "taxonomy": "iptc-subjectcode",
    "label": "furnishings and furniture",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013000"
    }]
    }, {
    "id": "15050007",
    "taxonomy": "iptc-subjectcode",
    "label": "Finn",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "15005026",
    "taxonomy": "iptc-subjectcode",
    "label": "javelin throw",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005026"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "04007004",
    "taxonomy": "iptc-subjectcode",
    "label": "mail order",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "11006007",
    "taxonomy": "iptc-subjectcode",
    "label": "government departments",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "02008003",
    "taxonomy": "iptc-subjectcode",
    "label": "court preliminary",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02008003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02008000"
    }]
    }, {
    "id": "15034001",
    "taxonomy": "iptc-subjectcode",
    "label": "sparring",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15034001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15034000"
    }]
    }, {
    "id": "12001000",
    "taxonomy": "iptc-subjectcode",
    "label": "cult and sect",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "11001002",
    "taxonomy": "iptc-subjectcode",
    "label": "national security",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001000"
    }]
    }, {
    "id": "15052002",
    "taxonomy": "iptc-subjectcode",
    "label": "K120 jump",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15052002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15052000"
    }]
    }, {
    "id": "15067001",
    "taxonomy": "iptc-subjectcode",
    "label": "beach volleyball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15067001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15067000"
    }]
    }, {
    "id": "13004005",
    "taxonomy": "iptc-subjectcode",
    "label": "zoology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004000"
    }]
    }, {
    "id": "09016000",
    "taxonomy": "iptc-subjectcode",
    "label": "employee",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "04004000",
    "taxonomy": "iptc-subjectcode",
    "label": "construction and property",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "10003000",
    "taxonomy": "iptc-subjectcode",
    "label": "gastronomy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "15041011",
    "taxonomy": "iptc-subjectcode",
    "label": "250 cm3",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "15014023",
    "taxonomy": "iptc-subjectcode",
    "label": "French boxing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014023"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "15099000",
    "taxonomy": "iptc-subjectcode",
    "label": "wushu",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15099000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "08007000",
    "taxonomy": "iptc-subjectcode",
    "label": "imperial and royal matters",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08000000"
    }]
    }, {
    "id": "06009000",
    "taxonomy": "iptc-subjectcode",
    "label": "waste",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "10004000",
    "taxonomy": "iptc-subjectcode",
    "label": "hobby",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "04004005",
    "taxonomy": "iptc-subjectcode",
    "label": "land price",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004000"
    }]
    }, {
    "id": "05011001",
    "taxonomy": "iptc-subjectcode",
    "label": "parochial school",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05011001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05011000"
    }]
    }, {
    "id": "15047006",
    "taxonomy": "iptc-subjectcode",
    "label": "eight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047000"
    }]
    }, {
    "id": "13015000",
    "taxonomy": "iptc-subjectcode",
    "label": "weather science",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "15005043",
    "taxonomy": "iptc-subjectcode",
    "label": "1500 m walk",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005043"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15073014",
    "taxonomy": "iptc-subjectcode",
    "label": "SouthPacific Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15064004",
    "taxonomy": "iptc-subjectcode",
    "label": "58-68 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064000"
    }]
    }, {
    "id": "04010009",
    "taxonomy": "iptc-subjectcode",
    "label": "satellite and cable service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "15056014",
    "taxonomy": "iptc-subjectcode",
    "label": "st 5000m relay",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "15073025",
    "taxonomy": "iptc-subjectcode",
    "label": "league cup",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073025"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "04008010",
    "taxonomy": "iptc-subjectcode",
    "label": "international economic institution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15015001",
    "taxonomy": "iptc-subjectcode",
    "label": "Slalom",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "15062005",
    "taxonomy": "iptc-subjectcode",
    "label": "800 m freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "15014020",
    "taxonomy": "iptc-subjectcode",
    "label": "WBA",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014020"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "07014000",
    "taxonomy": "iptc-subjectcode",
    "label": "medical specialisation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "04016003",
    "taxonomy": "iptc-subjectcode",
    "label": "annual report",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "07014001",
    "taxonomy": "iptc-subjectcode",
    "label": "geriatric",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014000"
    }]
    }, {
    "id": "03013000",
    "taxonomy": "iptc-subjectcode",
    "label": "accident (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "12006000",
    "taxonomy": "iptc-subjectcode",
    "label": "values",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "12025004",
    "taxonomy": "iptc-subjectcode",
    "label": "ritual",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12025004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12025000"
    }]
    }, {
    "id": "09011000",
    "taxonomy": "iptc-subjectcode",
    "label": "wage and pension",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "04004004",
    "taxonomy": "iptc-subjectcode",
    "label": "farms",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004000"
    }]
    }, {
    "id": "15066000",
    "taxonomy": "iptc-subjectcode",
    "label": "triathlon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15066000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "14000000",
    "taxonomy": "iptc-subjectcode",
    "label": "social issue",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15014012",
    "taxonomy": "iptc-subjectcode",
    "label": "featherweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "13019000",
    "taxonomy": "iptc-subjectcode",
    "label": "biotechnology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13019000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "07001009",
    "taxonomy": "iptc-subjectcode",
    "label": "retrovirus",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001000"
    }]
    }, {
    "id": "03015002",
    "taxonomy": "iptc-subjectcode",
    "label": "avalanche/landslide",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03015002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03015000"
    }]
    }, {
    "id": "02012004",
    "taxonomy": "iptc-subjectcode",
    "label": "breach of contract",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012000"
    }]
    }, {
    "id": "15015012",
    "taxonomy": "iptc-subjectcode",
    "label": "pontoniering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "04016021",
    "taxonomy": "iptc-subjectcode",
    "label": "global expansion",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016021"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15062004",
    "taxonomy": "iptc-subjectcode",
    "label": "400 m freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "11010000",
    "taxonomy": "iptc-subjectcode",
    "label": "parties and movements",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "15025002",
    "taxonomy": "iptc-subjectcode",
    "label": "pairs",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15025002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15025000"
    }]
    }, {
    "id": "15070009",
    "taxonomy": "iptc-subjectcode",
    "label": "62 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "04016013",
    "taxonomy": "iptc-subjectcode",
    "label": "contract",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "17004000",
    "taxonomy": "iptc-subjectcode",
    "label": "statistic",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17000000"
    }]
    }, {
    "id": "04006014",
    "taxonomy": "iptc-subjectcode",
    "label": "janitorial service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "02001005",
    "taxonomy": "iptc-subjectcode",
    "label": "sexual assault",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }]
    }, {
    "id": "15005047",
    "taxonomy": "iptc-subjectcode",
    "label": "50 m hurdles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005047"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "13021000",
    "taxonomy": "iptc-subjectcode",
    "label": "nanotechnology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13021000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "03001000",
    "taxonomy": "iptc-subjectcode",
    "label": "drought",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "04003007",
    "taxonomy": "iptc-subjectcode",
    "label": "telecommunication service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003000"
    }]
    }, {
    "id": "04011006",
    "taxonomy": "iptc-subjectcode",
    "label": "industrial component",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011000"
    }]
    }, {
    "id": "15077007",
    "taxonomy": "iptc-subjectcode",
    "label": "SCF",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }]
    }, {
    "id": "15033003",
    "taxonomy": "iptc-subjectcode",
    "label": "middleweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033000"
    }]
    }, {
    "id": "15005036",
    "taxonomy": "iptc-subjectcode",
    "label": "15 km walk",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005036"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "03002000",
    "taxonomy": "iptc-subjectcode",
    "label": "earthquake",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "04016032",
    "taxonomy": "iptc-subjectcode",
    "label": "plant closing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016032"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "01011005",
    "taxonomy": "iptc-subjectcode",
    "label": "country music",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011000"
    }]
    }, {
    "id": "15043006",
    "taxonomy": "iptc-subjectcode",
    "label": "15 km pursuit free style",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "07003005",
    "taxonomy": "iptc-subjectcode",
    "label": "therapy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003000"
    }]
    }, {
    "id": "09013000",
    "taxonomy": "iptc-subjectcode",
    "label": "health and safety at work",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "15024001",
    "taxonomy": "iptc-subjectcode",
    "label": "roll hockey",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15024001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15024000"
    }]
    }, {
    "id": "11003007",
    "taxonomy": "iptc-subjectcode",
    "label": "voting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }]
    }, {
    "id": "15072007",
    "taxonomy": "iptc-subjectcode",
    "label": "76 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "13010002",
    "taxonomy": "iptc-subjectcode",
    "label": "laser",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13010002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13010000"
    }]
    }, {
    "id": "15039002",
    "taxonomy": "iptc-subjectcode",
    "label": "F3000",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039000"
    }]
    }, {
    "id": "15009000",
    "taxonomy": "iptc-subjectcode",
    "label": "biathlon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15064002",
    "taxonomy": "iptc-subjectcode",
    "label": "under 58 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064000"
    }]
    }, {
    "id": "15073004",
    "taxonomy": "iptc-subjectcode",
    "label": "Winter Universiade",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "01021000",
    "taxonomy": "iptc-subjectcode",
    "label": "entertainment (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01021000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "07016000",
    "taxonomy": "iptc-subjectcode",
    "label": "physical fitness",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "04008007",
    "taxonomy": "iptc-subjectcode",
    "label": "government aid",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "14006003",
    "taxonomy": "iptc-subjectcode",
    "label": "marriage",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006000"
    }]
    }, {
    "id": "15038001",
    "taxonomy": "iptc-subjectcode",
    "label": "running",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038000"
    }]
    }, {
    "id": "01004000",
    "taxonomy": "iptc-subjectcode",
    "label": "festive event (including carnival)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "11016007",
    "taxonomy": "iptc-subjectcode",
    "label": "planning inquiries",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016000"
    }]
    }, {
    "id": "15073041",
    "taxonomy": "iptc-subjectcode",
    "label": "inter-nations competition",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073041"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "02012003",
    "taxonomy": "iptc-subjectcode",
    "label": "restraint of trade",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012000"
    }]
    }, {
    "id": "07006001",
    "taxonomy": "iptc-subjectcode",
    "label": "primary care physician",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07006000"
    }]
    }, {
    "id": "07002000",
    "taxonomy": "iptc-subjectcode",
    "label": "epidemic and plague",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "15008004",
    "taxonomy": "iptc-subjectcode",
    "label": "German netball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008000"
    }]
    }, {
    "id": "16008000",
    "taxonomy": "iptc-subjectcode",
    "label": "demonstration",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "04006008",
    "taxonomy": "iptc-subjectcode",
    "label": "market research",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "01026003",
    "taxonomy": "iptc-subjectcode",
    "label": "newspapers",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01026003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01026000"
    }]
    }, {
    "id": "15010003",
    "taxonomy": "iptc-subjectcode",
    "label": "14-Jan",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010000"
    }]
    }, {
    "id": "15019017",
    "taxonomy": "iptc-subjectcode",
    "label": "Vtt-downhill",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019017"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "04016002",
    "taxonomy": "iptc-subjectcode",
    "label": "annual and special corporate meeting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "05005002",
    "taxonomy": "iptc-subjectcode",
    "label": "middle schools",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05005002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05005000"
    }]
    }, {
    "id": "15072011",
    "taxonomy": "iptc-subjectcode",
    "label": "54 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "05011003",
    "taxonomy": "iptc-subjectcode",
    "label": "yeshiva",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05011003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05011000"
    }]
    }, {
    "id": "03010002",
    "taxonomy": "iptc-subjectcode",
    "label": "railway accident",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03010002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03010000"
    }]
    }, {
    "id": "15026003",
    "taxonomy": "iptc-subjectcode",
    "label": "artistic skiing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15026003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15026000"
    }]
    }, {
    "id": "04005013",
    "taxonomy": "iptc-subjectcode",
    "label": "diesel fuel",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "15039007",
    "taxonomy": "iptc-subjectcode",
    "label": "NASCAR",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039000"
    }]
    }, {
    "id": "14016000",
    "taxonomy": "iptc-subjectcode",
    "label": "abortion",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15041003",
    "taxonomy": "iptc-subjectcode",
    "label": "grass-track",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "15028009",
    "taxonomy": "iptc-subjectcode",
    "label": "rhythmic",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "15050011",
    "taxonomy": "iptc-subjectcode",
    "label": "staging race",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "12015001",
    "taxonomy": "iptc-subjectcode",
    "label": "pope",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12015001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12015000"
    }]
    }, {
    "id": "12009005",
    "taxonomy": "iptc-subjectcode",
    "label": "methodist",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "15062009",
    "taxonomy": "iptc-subjectcode",
    "label": "relay 4x200 m freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "04008026",
    "taxonomy": "iptc-subjectcode",
    "label": "stocks",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008026"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15001000",
    "taxonomy": "iptc-subjectcode",
    "label": "aero and aviation sport",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "01018001",
    "taxonomy": "iptc-subjectcode",
    "label": "institution-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01018001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01018000"
    }]
    }, {
    "id": "14019000",
    "taxonomy": "iptc-subjectcode",
    "label": "juvenile delinquency",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14019000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "02007001",
    "taxonomy": "iptc-subjectcode",
    "label": "civil rights",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02007001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02007000"
    }]
    }, {
    "id": "10002000",
    "taxonomy": "iptc-subjectcode",
    "label": "gaming and lottery",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "11016003",
    "taxonomy": "iptc-subjectcode",
    "label": "pension and welfare",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016000"
    }]
    }, {
    "id": "02002000",
    "taxonomy": "iptc-subjectcode",
    "label": "judiciary (system of justice)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "06006006",
    "taxonomy": "iptc-subjectcode",
    "label": "rivers",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006000"
    }]
    }, {
    "id": "08003005",
    "taxonomy": "iptc-subjectcode",
    "label": "fortune-telling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003000"
    }]
    }, {
    "id": "15051006",
    "taxonomy": "iptc-subjectcode",
    "label": "50 m free pistol",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "15005007",
    "taxonomy": "iptc-subjectcode",
    "label": "mile",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15014016",
    "taxonomy": "iptc-subjectcode",
    "label": "flyweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "10014000",
    "taxonomy": "iptc-subjectcode",
    "label": "auto trends",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "15047002",
    "taxonomy": "iptc-subjectcode",
    "label": "double sculls",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047000"
    }]
    }, {
    "id": "02011001",
    "taxonomy": "iptc-subjectcode",
    "label": "international court or tribunal",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02011001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02011000"
    }]
    }, {
    "id": "13018000",
    "taxonomy": "iptc-subjectcode",
    "label": "mathematics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13018000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "15019006",
    "taxonomy": "iptc-subjectcode",
    "label": "points race",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15041009",
    "taxonomy": "iptc-subjectcode",
    "label": "superbike",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "02001001",
    "taxonomy": "iptc-subjectcode",
    "label": "homicide",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }]
    }, {
    "id": "15062000",
    "taxonomy": "iptc-subjectcode",
    "label": "swimming",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15062023",
    "taxonomy": "iptc-subjectcode",
    "label": "relay4x100 m medley",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062023"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "16003000",
    "taxonomy": "iptc-subjectcode",
    "label": "civil unrest",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "15074002",
    "taxonomy": "iptc-subjectcode",
    "label": "calf roping",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074000"
    }]
    }, {
    "id": "04002001",
    "taxonomy": "iptc-subjectcode",
    "label": "biotechnology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002000"
    }]
    }, {
    "id": "11002000",
    "taxonomy": "iptc-subjectcode",
    "label": "diplomacy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "07007003",
    "taxonomy": "iptc-subjectcode",
    "label": "western",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07007003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07007000"
    }]
    }, {
    "id": "04012001",
    "taxonomy": "iptc-subjectcode",
    "label": "building material",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012000"
    }]
    }, {
    "id": "04010002",
    "taxonomy": "iptc-subjectcode",
    "label": "book",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "02014000",
    "taxonomy": "iptc-subjectcode",
    "label": "inquest",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "07001002",
    "taxonomy": "iptc-subjectcode",
    "label": "virus diseases",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001000"
    }]
    }, {
    "id": "13004001",
    "taxonomy": "iptc-subjectcode",
    "label": "geology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004000"
    }]
    }, {
    "id": "02013000",
    "taxonomy": "iptc-subjectcode",
    "label": "war crime",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "15043017",
    "taxonomy": "iptc-subjectcode",
    "label": "50 km classic style",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043017"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "04009001",
    "taxonomy": "iptc-subjectcode",
    "label": "energy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04009001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04009000"
    }]
    }, {
    "id": "12009013",
    "taxonomy": "iptc-subjectcode",
    "label": "salvation army",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "02006000",
    "taxonomy": "iptc-subjectcode",
    "label": "laws",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "15005029",
    "taxonomy": "iptc-subjectcode",
    "label": "4x200 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005029"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "14007000",
    "taxonomy": "iptc-subjectcode",
    "label": "family planning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "04006021",
    "taxonomy": "iptc-subjectcode",
    "label": "printing/promotional service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006021"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15023002",
    "taxonomy": "iptc-subjectcode",
    "label": "foil",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15023002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15023000"
    }]
    }, {
    "id": "03005000",
    "taxonomy": "iptc-subjectcode",
    "label": "flood",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "12023000",
    "taxonomy": "iptc-subjectcode",
    "label": "religious text",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12023000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "13013000",
    "taxonomy": "iptc-subjectcode",
    "label": "micro science",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "07008001",
    "taxonomy": "iptc-subjectcode",
    "label": "vaccines",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07008001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07008000"
    }]
    }, {
    "id": "10004001",
    "taxonomy": "iptc-subjectcode",
    "label": "DIY",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10004001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10004000"
    }]
    }, {
    "id": "07014003",
    "taxonomy": "iptc-subjectcode",
    "label": "reproduction",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014000"
    }]
    }, {
    "id": "15007003",
    "taxonomy": "iptc-subjectcode",
    "label": "Major League Baseball (North American Professional) - Special (e.g. All-Star, World Series)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007000"
    }]
    }, {
    "id": "11001004",
    "taxonomy": "iptc-subjectcode",
    "label": "armed Forces",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001000"
    }]
    }, {
    "id": "09012000",
    "taxonomy": "iptc-subjectcode",
    "label": "work relations",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "04016009",
    "taxonomy": "iptc-subjectcode",
    "label": "buyback",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15074003",
    "taxonomy": "iptc-subjectcode",
    "label": "bull riding",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074000"
    }]
    }, {
    "id": "04008015",
    "taxonomy": "iptc-subjectcode",
    "label": "trade dispute",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "06013000",
    "taxonomy": "iptc-subjectcode",
    "label": "environmental cleanup",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "10009000",
    "taxonomy": "iptc-subjectcode",
    "label": "lifestyle (house and home)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "16009001",
    "taxonomy": "iptc-subjectcode",
    "label": "civil war",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16009001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16009000"
    }]
    }, {
    "id": "04003009",
    "taxonomy": "iptc-subjectcode",
    "label": "wireless technology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003000"
    }]
    }, {
    "id": "15005018",
    "taxonomy": "iptc-subjectcode",
    "label": "3000 m steeplechase",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005018"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15083000",
    "taxonomy": "iptc-subjectcode",
    "label": "skeleton",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15083000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15004002",
    "taxonomy": "iptc-subjectcode",
    "label": "crossbow shooting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15004002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15004000"
    }]
    }, {
    "id": "04008018",
    "taxonomy": "iptc-subjectcode",
    "label": "currency values",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008018"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15028015",
    "taxonomy": "iptc-subjectcode",
    "label": "trampoline",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "04016027",
    "taxonomy": "iptc-subjectcode",
    "label": "litigation and regulation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016027"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15040000",
    "taxonomy": "iptc-subjectcode",
    "label": "motor rallying",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15040000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04011001",
    "taxonomy": "iptc-subjectcode",
    "label": "aerospace",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011000"
    }]
    }, {
    "id": "15046001",
    "taxonomy": "iptc-subjectcode",
    "label": "F1",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15046001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15046000"
    }]
    }, {
    "id": "15062012",
    "taxonomy": "iptc-subjectcode",
    "label": "200 m backstroke",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "03003000",
    "taxonomy": "iptc-subjectcode",
    "label": "famine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "11027000",
    "taxonomy": "iptc-subjectcode",
    "label": "treaty",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11027000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "07004000",
    "taxonomy": "iptc-subjectcode",
    "label": "health organisations",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "04013002",
    "taxonomy": "iptc-subjectcode",
    "label": "food",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013000"
    }]
    }, {
    "id": "04016043",
    "taxonomy": "iptc-subjectcode",
    "label": "productivity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016043"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "04001000",
    "taxonomy": "iptc-subjectcode",
    "label": "agriculture",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "12004000",
    "taxonomy": "iptc-subjectcode",
    "label": "religion-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15069004",
    "taxonomy": "iptc-subjectcode",
    "label": "combined",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15069004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15069000"
    }]
    }, {
    "id": "15029000",
    "taxonomy": "iptc-subjectcode",
    "label": "handball (team)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15029000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "09003001",
    "taxonomy": "iptc-subjectcode",
    "label": "labor market",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09003000"
    }]
    }, {
    "id": "03012000",
    "taxonomy": "iptc-subjectcode",
    "label": "relief and aid organisation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "15061000",
    "taxonomy": "iptc-subjectcode",
    "label": "surfing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15061000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04016050",
    "taxonomy": "iptc-subjectcode",
    "label": "credit ratings",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016050"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "11014002",
    "taxonomy": "iptc-subjectcode",
    "label": "peace negotiations-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11014002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11014000"
    }]
    }, {
    "id": "15018000",
    "taxonomy": "iptc-subjectcode",
    "label": "curling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15018000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15072001",
    "taxonomy": "iptc-subjectcode",
    "label": "freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "01022001",
    "taxonomy": "iptc-subjectcode",
    "label": "cultural development",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01022001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01022000"
    }]
    }, {
    "id": "15032002",
    "taxonomy": "iptc-subjectcode",
    "label": "jai-alai",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "06006002",
    "taxonomy": "iptc-subjectcode",
    "label": "parks",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006000"
    }]
    }, {
    "id": "11019000",
    "taxonomy": "iptc-subjectcode",
    "label": "referenda",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11019000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "15021005",
    "taxonomy": "iptc-subjectcode",
    "label": "subaquatics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021000"
    }]
    }, {
    "id": "13002001",
    "taxonomy": "iptc-subjectcode",
    "label": "material science",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13002001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13002000"
    }]
    }, {
    "id": "11006010",
    "taxonomy": "iptc-subjectcode",
    "label": "public employees",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "15005058",
    "taxonomy": "iptc-subjectcode",
    "label": "440 yards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005058"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15038005",
    "taxonomy": "iptc-subjectcode",
    "label": "showjumping",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038000"
    }]
    }, {
    "id": "15005044",
    "taxonomy": "iptc-subjectcode",
    "label": "2000 m walk",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005044"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "08003001",
    "taxonomy": "iptc-subjectcode",
    "label": "advice",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003000"
    }]
    }, {
    "id": "15064005",
    "taxonomy": "iptc-subjectcode",
    "label": "57-67 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064000"
    }]
    }, {
    "id": "14025002",
    "taxonomy": "iptc-subjectcode",
    "label": "social problems",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025000"
    }]
    }, {
    "id": "07003004",
    "taxonomy": "iptc-subjectcode",
    "label": "medical procedure/test",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003000"
    }]
    }, {
    "id": "06001000",
    "taxonomy": "iptc-subjectcode",
    "label": "renewable energy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "04016010",
    "taxonomy": "iptc-subjectcode",
    "label": "C.E.O. interview",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15032007",
    "taxonomy": "iptc-subjectcode",
    "label": "chistera corta",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "15022003",
    "taxonomy": "iptc-subjectcode",
    "label": "jumping",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15022003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15022000"
    }]
    }, {
    "id": "15043001",
    "taxonomy": "iptc-subjectcode",
    "label": "cross-country",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "02003000",
    "taxonomy": "iptc-subjectcode",
    "label": "police",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "04000000",
    "taxonomy": "iptc-subjectcode",
    "label": "economy, business and finance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "11003000",
    "taxonomy": "iptc-subjectcode",
    "label": "election",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "03017000",
    "taxonomy": "iptc-subjectcode",
    "label": "rescue",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03017000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "15026000",
    "taxonomy": "iptc-subjectcode",
    "label": "freestyle Skiing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15026000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04008009",
    "taxonomy": "iptc-subjectcode",
    "label": "interest rate",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "04012005",
    "taxonomy": "iptc-subjectcode",
    "label": "mining",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012000"
    }]
    }, {
    "id": "07013001",
    "taxonomy": "iptc-subjectcode",
    "label": "food safety",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07013001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07013000"
    }]
    }, {
    "id": "02000000",
    "taxonomy": "iptc-subjectcode",
    "label": "crime, law and justice",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "15012000",
    "taxonomy": "iptc-subjectcode",
    "label": "bowling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04016053",
    "taxonomy": "iptc-subjectcode",
    "label": "recalls (products)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016053"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15073030",
    "taxonomy": "iptc-subjectcode",
    "label": "continental championship 3rd level",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073030"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "04010003",
    "taxonomy": "iptc-subjectcode",
    "label": "cinema industry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "04016016",
    "taxonomy": "iptc-subjectcode",
    "label": "earnings forecast",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15019010",
    "taxonomy": "iptc-subjectcode",
    "label": "one hour",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "14024005",
    "taxonomy": "iptc-subjectcode",
    "label": "senior citizens",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024000"
    }]
    }, {
    "id": "11001005",
    "taxonomy": "iptc-subjectcode",
    "label": "military equipment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001000"
    }]
    }, {
    "id": "15014013",
    "taxonomy": "iptc-subjectcode",
    "label": "super-bantamweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "12009000",
    "taxonomy": "iptc-subjectcode",
    "label": "christianity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "04008002",
    "taxonomy": "iptc-subjectcode",
    "label": "consumer issue",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "04008029",
    "taxonomy": "iptc-subjectcode",
    "label": "derivative securities",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008029"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "09006000",
    "taxonomy": "iptc-subjectcode",
    "label": "retirement",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "15014005",
    "taxonomy": "iptc-subjectcode",
    "label": "super-middleweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "04012000",
    "taxonomy": "iptc-subjectcode",
    "label": "metal and mineral",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "15044000",
    "taxonomy": "iptc-subjectcode",
    "label": "orienteering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15044000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15014024",
    "taxonomy": "iptc-subjectcode",
    "label": "Thai boxing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014024"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "04016005",
    "taxonomy": "iptc-subjectcode",
    "label": "merger, acquisition and takeover",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15077002",
    "taxonomy": "iptc-subjectcode",
    "label": "guts",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }]
    }, {
    "id": "11026000",
    "taxonomy": "iptc-subjectcode",
    "label": "freedom of religion",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11026000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "01016001",
    "taxonomy": "iptc-subjectcode",
    "label": "soap opera",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01016001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01016000"
    }]
    }, {
    "id": "11002003",
    "taxonomy": "iptc-subjectcode",
    "label": "peace negotiations",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11002003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11002000"
    }]
    }, {
    "id": "15073022",
    "taxonomy": "iptc-subjectcode",
    "label": "National Cup",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073022"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "03006000",
    "taxonomy": "iptc-subjectcode",
    "label": "industrial accident",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "15040001",
    "taxonomy": "iptc-subjectcode",
    "label": "rallying",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15040001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15040000"
    }]
    }, {
    "id": "15036001",
    "taxonomy": "iptc-subjectcode",
    "label": "singles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15036001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15036000"
    }]
    }, {
    "id": "03009000",
    "taxonomy": "iptc-subjectcode",
    "label": "pollution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "11001008",
    "taxonomy": "iptc-subjectcode",
    "label": "missile systems",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001000"
    }]
    }, {
    "id": "15074007",
    "taxonomy": "iptc-subjectcode",
    "label": "goat roping",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074000"
    }]
    }, {
    "id": "04001001",
    "taxonomy": "iptc-subjectcode",
    "label": "arable farming",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001000"
    }]
    }, {
    "id": "04014003",
    "taxonomy": "iptc-subjectcode",
    "label": "recreational and sporting goods",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014000"
    }]
    }, {
    "id": "13003005",
    "taxonomy": "iptc-subjectcode",
    "label": "anthropology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003000"
    }]
    }, {
    "id": "04016038",
    "taxonomy": "iptc-subjectcode",
    "label": "quarterly or semiannual financial statement",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016038"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "01027000",
    "taxonomy": "iptc-subjectcode",
    "label": "internet",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01027000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15015002",
    "taxonomy": "iptc-subjectcode",
    "label": "200 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "15018001",
    "taxonomy": "iptc-subjectcode",
    "label": "icestock sport",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15018001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15018000"
    }]
    }, {
    "id": "15005014",
    "taxonomy": "iptc-subjectcode",
    "label": "25000",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15073033",
    "taxonomy": "iptc-subjectcode",
    "label": "national championship3rdlevel",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073033"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15062015",
    "taxonomy": "iptc-subjectcode",
    "label": "200 m breaststroke",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "04016042",
    "taxonomy": "iptc-subjectcode",
    "label": "industrial production",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016042"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "04002006",
    "taxonomy": "iptc-subjectcode",
    "label": "pharmaceutical",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002000"
    }]
    }, {
    "id": "15014002",
    "taxonomy": "iptc-subjectcode",
    "label": "heavyweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "12006001",
    "taxonomy": "iptc-subjectcode",
    "label": "ethics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12006000"
    }]
    }, {
    "id": "01020000",
    "taxonomy": "iptc-subjectcode",
    "label": "arts (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01020000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15038004",
    "taxonomy": "iptc-subjectcode",
    "label": "fencing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038000"
    }]
    }, {
    "id": "04013006",
    "taxonomy": "iptc-subjectcode",
    "label": "soft drinks",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013000"
    }]
    }, {
    "id": "14024002",
    "taxonomy": "iptc-subjectcode",
    "label": "infants",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024000"
    }]
    }, {
    "id": "11003002",
    "taxonomy": "iptc-subjectcode",
    "label": "political campaigns",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }]
    }, {
    "id": "15050009",
    "taxonomy": "iptc-subjectcode",
    "label": "flying dutchmann",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "08005002",
    "taxonomy": "iptc-subjectcode",
    "label": "death",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005000"
    }]
    }, {
    "id": "11017000",
    "taxonomy": "iptc-subjectcode",
    "label": "migration",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11017000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "15056002",
    "taxonomy": "iptc-subjectcode",
    "label": "1000 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "15062022",
    "taxonomy": "iptc-subjectcode",
    "label": "relay 4x50 m medlay",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062022"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "15062001",
    "taxonomy": "iptc-subjectcode",
    "label": "50 m freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "07001005",
    "taxonomy": "iptc-subjectcode",
    "label": "heart disease",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001000"
    }]
    }, {
    "id": "04005014",
    "taxonomy": "iptc-subjectcode",
    "label": "kerosene/paraffin",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "15064008",
    "taxonomy": "iptc-subjectcode",
    "label": "over 80 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064000"
    }]
    }, {
    "id": "01006000",
    "taxonomy": "iptc-subjectcode",
    "label": "dance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15005069",
    "taxonomy": "iptc-subjectcode",
    "label": "pentathlon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005069"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15074001",
    "taxonomy": "iptc-subjectcode",
    "label": "barrel racing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074000"
    }]
    }, {
    "id": "04013001",
    "taxonomy": "iptc-subjectcode",
    "label": "distiller and brewer",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013000"
    }]
    }, {
    "id": "15030001",
    "taxonomy": "iptc-subjectcode",
    "label": "flat racing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15030001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15030000"
    }]
    }, {
    "id": "04018000",
    "taxonomy": "iptc-subjectcode",
    "label": "business (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04018000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "16003001",
    "taxonomy": "iptc-subjectcode",
    "label": "revolutions",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003000"
    }]
    }, {
    "id": "15019021",
    "taxonomy": "iptc-subjectcode",
    "label": "cycle ball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019021"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15069000",
    "taxonomy": "iptc-subjectcode",
    "label": "water skiing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15069000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "08002000",
    "taxonomy": "iptc-subjectcode",
    "label": "curiosity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08000000"
    }]
    }, {
    "id": "15062008",
    "taxonomy": "iptc-subjectcode",
    "label": "relay 4x100 m freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "15015006",
    "taxonomy": "iptc-subjectcode",
    "label": "K2",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "02001009",
    "taxonomy": "iptc-subjectcode",
    "label": "gang activity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }]
    }, {
    "id": "06002000",
    "taxonomy": "iptc-subjectcode",
    "label": "conservation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "15047007",
    "taxonomy": "iptc-subjectcode",
    "label": "lightweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047000"
    }]
    }, {
    "id": "07017001",
    "taxonomy": "iptc-subjectcode",
    "label": "mental illness",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07017001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07017000"
    }]
    }, {
    "id": "15073015",
    "taxonomy": "iptc-subjectcode",
    "label": "PanArabic Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "04006018",
    "taxonomy": "iptc-subjectcode",
    "label": "personal finance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006018"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15019000",
    "taxonomy": "iptc-subjectcode",
    "label": "cycling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "10001002",
    "taxonomy": "iptc-subjectcode",
    "label": "chess",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10001002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10001000"
    }]
    }, {
    "id": "14014000",
    "taxonomy": "iptc-subjectcode",
    "label": "racism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15043010",
    "taxonomy": "iptc-subjectcode",
    "label": "50 km free style",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "04005007",
    "taxonomy": "iptc-subjectcode",
    "label": "waste management and pollution control",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "04016057",
    "taxonomy": "iptc-subjectcode",
    "label": "new service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016057"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "06005000",
    "taxonomy": "iptc-subjectcode",
    "label": "environmental pollution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "09003004",
    "taxonomy": "iptc-subjectcode",
    "label": "occupations",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09003004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09003000"
    }]
    }, {
    "id": "04003003",
    "taxonomy": "iptc-subjectcode",
    "label": "satellite technology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003000"
    }]
    }, {
    "id": "07003000",
    "taxonomy": "iptc-subjectcode",
    "label": "health treatment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "12009011",
    "taxonomy": "iptc-subjectcode",
    "label": "old catholic",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "02003003",
    "taxonomy": "iptc-subjectcode",
    "label": "arrest",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02003003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02003000"
    }]
    }, {
    "id": "15003000",
    "taxonomy": "iptc-subjectcode",
    "label": "American football",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "01011001",
    "taxonomy": "iptc-subjectcode",
    "label": "classical music",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011000"
    }]
    }, {
    "id": "15005041",
    "taxonomy": "iptc-subjectcode",
    "label": "5 km walk",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005041"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15051010",
    "taxonomy": "iptc-subjectcode",
    "label": "trap",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "11006008",
    "taxonomy": "iptc-subjectcode",
    "label": "public officials",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "15050004",
    "taxonomy": "iptc-subjectcode",
    "label": "Europe",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "02008002",
    "taxonomy": "iptc-subjectcode",
    "label": "arbitration",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02008002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02008000"
    }]
    }, {
    "id": "14022000",
    "taxonomy": "iptc-subjectcode",
    "label": "abusive behaviour",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14022000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "14012000",
    "taxonomy": "iptc-subjectcode",
    "label": "poverty",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15005001",
    "taxonomy": "iptc-subjectcode",
    "label": "100 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15034000",
    "taxonomy": "iptc-subjectcode",
    "label": "karate",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15034000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "03007000",
    "taxonomy": "iptc-subjectcode",
    "label": "meteorological disaster",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "12014003",
    "taxonomy": "iptc-subjectcode",
    "label": "pentecost",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014000"
    }]
    }, {
    "id": "15076000",
    "taxonomy": "iptc-subjectcode",
    "label": "bandy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15076000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "12023003",
    "taxonomy": "iptc-subjectcode",
    "label": "torah",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12023003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12023000"
    }]
    }, {
    "id": "15009004",
    "taxonomy": "iptc-subjectcode",
    "label": "20 km",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009000"
    }]
    }, {
    "id": "13004006",
    "taxonomy": "iptc-subjectcode",
    "label": "physiology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004000"
    }]
    }, {
    "id": "04016049",
    "taxonomy": "iptc-subjectcode",
    "label": "losses",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016049"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "01015001",
    "taxonomy": "iptc-subjectcode",
    "label": "plastic art",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01015001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01015000"
    }]
    }, {
    "id": "04016024",
    "taxonomy": "iptc-subjectcode",
    "label": "leveraged buyout",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016024"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "01026004",
    "taxonomy": "iptc-subjectcode",
    "label": "reviews",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01026004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01026000"
    }]
    }, {
    "id": "15041014",
    "taxonomy": "iptc-subjectcode",
    "label": "motoGP",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "06006009",
    "taxonomy": "iptc-subjectcode",
    "label": "energy resources",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006000"
    }]
    }, {
    "id": "01010001",
    "taxonomy": "iptc-subjectcode",
    "label": "fiction",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01010001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01010000"
    }]
    }, {
    "id": "15071004",
    "taxonomy": "iptc-subjectcode",
    "label": "land",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15071004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15071000"
    }]
    }, {
    "id": "04010008",
    "taxonomy": "iptc-subjectcode",
    "label": "radio industry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "01023000",
    "taxonomy": "iptc-subjectcode",
    "label": "nightclub",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01023000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15021000",
    "taxonomy": "iptc-subjectcode",
    "label": "diving",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "06012000",
    "taxonomy": "iptc-subjectcode",
    "label": "hazardous materials",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "15073026",
    "taxonomy": "iptc-subjectcode",
    "label": "world championship",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073026"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "11006003",
    "taxonomy": "iptc-subjectcode",
    "label": "think tank",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "16005001",
    "taxonomy": "iptc-subjectcode",
    "label": "bioterrorism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16005001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16005000"
    }]
    }, {
    "id": "15056013",
    "taxonomy": "iptc-subjectcode",
    "label": "st 5000m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "15058002",
    "taxonomy": "iptc-subjectcode",
    "label": "international federation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058000"
    }]
    }, {
    "id": "15039003",
    "taxonomy": "iptc-subjectcode",
    "label": "endurance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039000"
    }]
    }, {
    "id": "15008000",
    "taxonomy": "iptc-subjectcode",
    "label": "basketball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15066001",
    "taxonomy": "iptc-subjectcode",
    "label": "triathlon swimming",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15066001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15066000"
    }]
    }, {
    "id": "02002003",
    "taxonomy": "iptc-subjectcode",
    "label": "court administration",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02002003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02002000"
    }]
    }, {
    "id": "06007000",
    "taxonomy": "iptc-subjectcode",
    "label": "nature",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "15041007",
    "taxonomy": "iptc-subjectcode",
    "label": "trial",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "15028005",
    "taxonomy": "iptc-subjectcode",
    "label": "parallel bars",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "04006004",
    "taxonomy": "iptc-subjectcode",
    "label": "employment agency",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "04001005",
    "taxonomy": "iptc-subjectcode",
    "label": "viniculture",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001000"
    }]
    }, {
    "id": "12021000",
    "taxonomy": "iptc-subjectcode",
    "label": "parsasm",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12021000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "04016046",
    "taxonomy": "iptc-subjectcode",
    "label": "corporations",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016046"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "12025000",
    "taxonomy": "iptc-subjectcode",
    "label": "religious event",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12025000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "04008022",
    "taxonomy": "iptc-subjectcode",
    "label": "mortgages",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008022"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "05007000",
    "taxonomy": "iptc-subjectcode",
    "label": "university",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "15070010",
    "taxonomy": "iptc-subjectcode",
    "label": "69 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "04005003",
    "taxonomy": "iptc-subjectcode",
    "label": "oil and gas - downstream activities",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "15062026",
    "taxonomy": "iptc-subjectcode",
    "label": "synchronised free routine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062026"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "02004002",
    "taxonomy": "iptc-subjectcode",
    "label": "execution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02004002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02004000"
    }]
    }, {
    "id": "02009000",
    "taxonomy": "iptc-subjectcode",
    "label": "prosecution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "15005055",
    "taxonomy": "iptc-subjectcode",
    "label": "100 yard hurdles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005055"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15005025",
    "taxonomy": "iptc-subjectcode",
    "label": "hammer throw",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005025"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15050015",
    "taxonomy": "iptc-subjectcode",
    "label": "yngling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "04007007",
    "taxonomy": "iptc-subjectcode",
    "label": "wholesale",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "14003001",
    "taxonomy": "iptc-subjectcode",
    "label": "population and census",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14003000"
    }]
    }, {
    "id": "04016035",
    "taxonomy": "iptc-subjectcode",
    "label": "proxy filing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016035"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15062019",
    "taxonomy": "iptc-subjectcode",
    "label": "100 m medley",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062019"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "01017001",
    "taxonomy": "iptc-subjectcode",
    "label": "music theatre",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01017001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01017000"
    }]
    }, {
    "id": "14006004",
    "taxonomy": "iptc-subjectcode",
    "label": "divorce",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006000"
    }]
    }, {
    "id": "15005003",
    "taxonomy": "iptc-subjectcode",
    "label": "400 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "13001003",
    "taxonomy": "iptc-subjectcode",
    "label": "cosmology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13001003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13001000"
    }]
    }, {
    "id": "15043012",
    "taxonomy": "iptc-subjectcode",
    "label": "4x10 km relay",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "15091000",
    "taxonomy": "iptc-subjectcode",
    "label": "snowbiking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15091000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15005066",
    "taxonomy": "iptc-subjectcode",
    "label": "3 miles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005066"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "10003001",
    "taxonomy": "iptc-subjectcode",
    "label": "organic foods",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10003000"
    }]
    }, {
    "id": "15072008",
    "taxonomy": "iptc-subjectcode",
    "label": "69 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "15060000",
    "taxonomy": "iptc-subjectcode",
    "label": "sumo wrestling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15060000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "14010002",
    "taxonomy": "iptc-subjectcode",
    "label": "national or ethnic minority",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14010002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14010000"
    }]
    }, {
    "id": "15073037",
    "taxonomy": "iptc-subjectcode",
    "label": "intercontinental tournament",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073037"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15005030",
    "taxonomy": "iptc-subjectcode",
    "label": "4x400 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005030"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15019002",
    "taxonomy": "iptc-subjectcode",
    "label": "pursuit",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "04017000",
    "taxonomy": "iptc-subjectcode",
    "label": "economy (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04017000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "09003000",
    "taxonomy": "iptc-subjectcode",
    "label": "employment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "15000000",
    "taxonomy": "iptc-subjectcode",
    "label": "sport",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "01018000",
    "taxonomy": "iptc-subjectcode",
    "label": "monument and heritage site",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01018000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15039001",
    "taxonomy": "iptc-subjectcode",
    "label": "Formula One",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039000"
    }]
    }, {
    "id": "04016044",
    "taxonomy": "iptc-subjectcode",
    "label": "inventories",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016044"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15062018",
    "taxonomy": "iptc-subjectcode",
    "label": "200 m butterfly",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062018"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "11006002",
    "taxonomy": "iptc-subjectcode",
    "label": "safety of citizens",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "10016000",
    "taxonomy": "iptc-subjectcode",
    "label": "beauty",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "15073011",
    "taxonomy": "iptc-subjectcode",
    "label": "Mediterranean Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "09000000",
    "taxonomy": "iptc-subjectcode",
    "label": "labour",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "07006000",
    "taxonomy": "iptc-subjectcode",
    "label": "medical staff",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "15047003",
    "taxonomy": "iptc-subjectcode",
    "label": "quadruple sculls",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047000"
    }]
    }, {
    "id": "13009000",
    "taxonomy": "iptc-subjectcode",
    "label": "science (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "05004000",
    "taxonomy": "iptc-subjectcode",
    "label": "preschool",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "14006002",
    "taxonomy": "iptc-subjectcode",
    "label": "adoption",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006000"
    }]
    }, {
    "id": "03000000",
    "taxonomy": "iptc-subjectcode",
    "label": "disaster and accident",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "10006000",
    "taxonomy": "iptc-subjectcode",
    "label": "tourism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "15073027",
    "taxonomy": "iptc-subjectcode",
    "label": "intercontinental championship",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073027"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "11025000",
    "taxonomy": "iptc-subjectcode",
    "label": "freedom of the press",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11025000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "04005012",
    "taxonomy": "iptc-subjectcode",
    "label": "petrol",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "02001006",
    "taxonomy": "iptc-subjectcode",
    "label": "assault (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }]
    }, {
    "id": "15008005",
    "taxonomy": "iptc-subjectcode",
    "label": "Dutch netball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008000"
    }]
    }, {
    "id": "15005017",
    "taxonomy": "iptc-subjectcode",
    "label": "400 m hurdles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005017"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15086000",
    "taxonomy": "iptc-subjectcode",
    "label": "duathlon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15086000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04011004",
    "taxonomy": "iptc-subjectcode",
    "label": "electrical appliance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011000"
    }]
    }, {
    "id": "15019018",
    "taxonomy": "iptc-subjectcode",
    "label": "bi-crossing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019018"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "16011000",
    "taxonomy": "iptc-subjectcode",
    "label": "crisis",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "09001000",
    "taxonomy": "iptc-subjectcode",
    "label": "apprentices",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "12015000",
    "taxonomy": "iptc-subjectcode",
    "label": "religious leader",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "14025000",
    "taxonomy": "iptc-subjectcode",
    "label": "social issues (general)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "11014001",
    "taxonomy": "iptc-subjectcode",
    "label": "international relations-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11014001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11014000"
    }]
    }, {
    "id": "12006002",
    "taxonomy": "iptc-subjectcode",
    "label": "corrupt practices",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12006002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12006000"
    }]
    }, {
    "id": "11024002",
    "taxonomy": "iptc-subjectcode",
    "label": "democracy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11024002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11024000"
    }]
    }, {
    "id": "12017000",
    "taxonomy": "iptc-subjectcode",
    "label": "taoism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12017000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "03010003",
    "taxonomy": "iptc-subjectcode",
    "label": "air and space accident",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03010003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03010000"
    }]
    }, {
    "id": "07009000",
    "taxonomy": "iptc-subjectcode",
    "label": "injury",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "15073009",
    "taxonomy": "iptc-subjectcode",
    "label": "Panamerican Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "13020000",
    "taxonomy": "iptc-subjectcode",
    "label": "agricultural research and technology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13020000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "02007000",
    "taxonomy": "iptc-subjectcode",
    "label": "justice and rights",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "05010003",
    "taxonomy": "iptc-subjectcode",
    "label": "curriculum",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05010003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05010000"
    }]
    }, {
    "id": "06006005",
    "taxonomy": "iptc-subjectcode",
    "label": "mountains",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006000"
    }]
    }, {
    "id": "11006006",
    "taxonomy": "iptc-subjectcode",
    "label": "heads of state",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "15005042",
    "taxonomy": "iptc-subjectcode",
    "label": "heptathlon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005042"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15015011",
    "taxonomy": "iptc-subjectcode",
    "label": "canoe sailing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "11016004",
    "taxonomy": "iptc-subjectcode",
    "label": "personal weapon control",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016000"
    }]
    }, {
    "id": "03014000",
    "taxonomy": "iptc-subjectcode",
    "label": "emergency incident",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "01005001",
    "taxonomy": "iptc-subjectcode",
    "label": "film festival",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01005001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01005000"
    }]
    }, {
    "id": "05011002",
    "taxonomy": "iptc-subjectcode",
    "label": "seminary",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05011002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05011000"
    }]
    }, {
    "id": "15050016",
    "taxonomy": "iptc-subjectcode",
    "label": "mistral",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "15051005",
    "taxonomy": "iptc-subjectcode",
    "label": "25 m sport pistol",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "07014002",
    "taxonomy": "iptc-subjectcode",
    "label": "pediatrics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07014000"
    }]
    }, {
    "id": "15073038",
    "taxonomy": "iptc-subjectcode",
    "label": "continental tournament",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073038"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15002003",
    "taxonomy": "iptc-subjectcode",
    "label": "super G",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002000"
    }]
    }, {
    "id": "15021006",
    "taxonomy": "iptc-subjectcode",
    "label": "scuba diving",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021000"
    }]
    }, {
    "id": "02011000",
    "taxonomy": "iptc-subjectcode",
    "label": "international law",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02000000"
    }]
    }, {
    "id": "15005031",
    "taxonomy": "iptc-subjectcode",
    "label": "4x800 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005031"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "11016006",
    "taxonomy": "iptc-subjectcode",
    "label": "personal data collection",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016000"
    }]
    }, {
    "id": "03004000",
    "taxonomy": "iptc-subjectcode",
    "label": "fire",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "15056001",
    "taxonomy": "iptc-subjectcode",
    "label": "500 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "04016055",
    "taxonomy": "iptc-subjectcode",
    "label": "consumers",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016055"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15033007",
    "taxonomy": "iptc-subjectcode",
    "label": "extra lightweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033000"
    }]
    }, {
    "id": "01005000",
    "taxonomy": "iptc-subjectcode",
    "label": "cinema",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "11002001",
    "taxonomy": "iptc-subjectcode",
    "label": "summit",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11002001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11002000"
    }]
    }, {
    "id": "04002000",
    "taxonomy": "iptc-subjectcode",
    "label": "chemicals",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "15008001",
    "taxonomy": "iptc-subjectcode",
    "label": "National Basketball Association (North American Professional)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15008000"
    }]
    }, {
    "id": "01009000",
    "taxonomy": "iptc-subjectcode",
    "label": "library and museum",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "04008017",
    "taxonomy": "iptc-subjectcode",
    "label": "prices",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008017"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "04006017",
    "taxonomy": "iptc-subjectcode",
    "label": "wedding service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006017"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "12011000",
    "taxonomy": "iptc-subjectcode",
    "label": "judaism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15009001",
    "taxonomy": "iptc-subjectcode",
    "label": "7.5 km",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009000"
    }]
    }, {
    "id": "15002000",
    "taxonomy": "iptc-subjectcode",
    "label": "alpine skiing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15035000",
    "taxonomy": "iptc-subjectcode",
    "label": "lacrosse",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15035000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04006002",
    "taxonomy": "iptc-subjectcode",
    "label": "banking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "04011007",
    "taxonomy": "iptc-subjectcode",
    "label": "instrument engineering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011000"
    }]
    }, {
    "id": "15051003",
    "taxonomy": "iptc-subjectcode",
    "label": "10 m running target",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "15043016",
    "taxonomy": "iptc-subjectcode",
    "label": "1.5 km sprint free",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "15041002",
    "taxonomy": "iptc-subjectcode",
    "label": "enduro",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "15050010",
    "taxonomy": "iptc-subjectcode",
    "label": "505",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "15033004",
    "taxonomy": "iptc-subjectcode",
    "label": "half-middleweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033000"
    }]
    }, {
    "id": "15082000",
    "taxonomy": "iptc-subjectcode",
    "label": "dog racing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15082000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15096000",
    "taxonomy": "iptc-subjectcode",
    "label": "kyudo",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15096000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15043005",
    "taxonomy": "iptc-subjectcode",
    "label": "15 km classical style",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "11024003",
    "taxonomy": "iptc-subjectcode",
    "label": "political development",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11024003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11024000"
    }]
    }, {
    "id": "11011000",
    "taxonomy": "iptc-subjectcode",
    "label": "refugee",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "12010000",
    "taxonomy": "iptc-subjectcode",
    "label": "islam",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "14021000",
    "taxonomy": "iptc-subjectcode",
    "label": "slavery",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14021000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15007006",
    "taxonomy": "iptc-subjectcode",
    "label": "World Series",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15007000"
    }]
    }, {
    "id": "15050001",
    "taxonomy": "iptc-subjectcode",
    "label": "Tornado",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "15042000",
    "taxonomy": "iptc-subjectcode",
    "label": "netball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15042000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15005068",
    "taxonomy": "iptc-subjectcode",
    "label": "4x1 mile",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005068"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15032003",
    "taxonomy": "iptc-subjectcode",
    "label": "left wall",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "04007001",
    "taxonomy": "iptc-subjectcode",
    "label": "clothing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "06006000",
    "taxonomy": "iptc-subjectcode",
    "label": "natural resources",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "05002000",
    "taxonomy": "iptc-subjectcode",
    "label": "further education",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "15014017",
    "taxonomy": "iptc-subjectcode",
    "label": "light flyweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014017"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "15064001",
    "taxonomy": "iptc-subjectcode",
    "label": "under 49 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15064000"
    }]
    }, {
    "id": "13017000",
    "taxonomy": "iptc-subjectcode",
    "label": "identification technology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13017000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "04010010",
    "taxonomy": "iptc-subjectcode",
    "label": "television industry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "04004003",
    "taxonomy": "iptc-subjectcode",
    "label": "real estate",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004000"
    }]
    }, {
    "id": "15044001",
    "taxonomy": "iptc-subjectcode",
    "label": "ski orienteering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15044001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15044000"
    }]
    }, {
    "id": "15005012",
    "taxonomy": "iptc-subjectcode",
    "label": "20 km",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "04016008",
    "taxonomy": "iptc-subjectcode",
    "label": "board of directors (appointment and change)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15065001",
    "taxonomy": "iptc-subjectcode",
    "label": "soft tennis",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15065001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15065000"
    }]
    }, {
    "id": "10012000",
    "taxonomy": "iptc-subjectcode",
    "label": "hunting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "15049001",
    "taxonomy": "iptc-subjectcode",
    "label": "rugby 7",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15049001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15049000"
    }]
    }, {
    "id": "04014004",
    "taxonomy": "iptc-subjectcode",
    "label": "restaurant and catering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014000"
    }]
    }, {
    "id": "15005052",
    "taxonomy": "iptc-subjectcode",
    "label": "60 yards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005052"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "04008012",
    "taxonomy": "iptc-subjectcode",
    "label": "loan market",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15010000",
    "taxonomy": "iptc-subjectcode",
    "label": "billiards, snooker and pool",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "01011006",
    "taxonomy": "iptc-subjectcode",
    "label": "rock and roll music",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011000"
    }]
    }, {
    "id": "15019007",
    "taxonomy": "iptc-subjectcode",
    "label": "Madison race",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "15077006",
    "taxonomy": "iptc-subjectcode",
    "label": "DDC",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }]
    }, {
    "id": "15073000",
    "taxonomy": "iptc-subjectcode",
    "label": "sports event",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "11006013",
    "taxonomy": "iptc-subjectcode",
    "label": "impeachment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "15046002",
    "taxonomy": "iptc-subjectcode",
    "label": "F2",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15046002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15046000"
    }]
    }, {
    "id": "01021001",
    "taxonomy": "iptc-subjectcode",
    "label": "entertainment award",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01021001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01021000"
    }]
    }, {
    "id": "07007004",
    "taxonomy": "iptc-subjectcode",
    "label": "traditional Chinese",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07007004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07007000"
    }]
    }, {
    "id": "04010007",
    "taxonomy": "iptc-subjectcode",
    "label": "public relation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04010000"
    }]
    }, {
    "id": "12002001",
    "taxonomy": "iptc-subjectcode",
    "label": "unificationism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12002001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12002000"
    }]
    }, {
    "id": "15050012",
    "taxonomy": "iptc-subjectcode",
    "label": "around the world",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "04006022",
    "taxonomy": "iptc-subjectcode",
    "label": "investment service",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006022"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15072012",
    "taxonomy": "iptc-subjectcode",
    "label": "Swiss wrestling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "04016033",
    "taxonomy": "iptc-subjectcode",
    "label": "plant opening",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016033"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15026002",
    "taxonomy": "iptc-subjectcode",
    "label": "aerials",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15026002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15026000"
    }]
    }, {
    "id": "04005001",
    "taxonomy": "iptc-subjectcode",
    "label": "alternative energy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "04016040",
    "taxonomy": "iptc-subjectcode",
    "label": "spin-off",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016040"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15005028",
    "taxonomy": "iptc-subjectcode",
    "label": "4x100 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005028"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15005053",
    "taxonomy": "iptc-subjectcode",
    "label": "60 yard hurdles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005053"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "04015001",
    "taxonomy": "iptc-subjectcode",
    "label": "air transport",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04015001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04015000"
    }]
    }, {
    "id": "15005035",
    "taxonomy": "iptc-subjectcode",
    "label": "10 km walk",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005035"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "02012002",
    "taxonomy": "iptc-subjectcode",
    "label": "embezzlement",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012000"
    }]
    }, {
    "id": "15014009",
    "taxonomy": "iptc-subjectcode",
    "label": "light-welterweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "02003002",
    "taxonomy": "iptc-subjectcode",
    "label": "investigation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02003002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02003000"
    }]
    }, {
    "id": "15079000",
    "taxonomy": "iptc-subjectcode",
    "label": "casting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15079000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15005023",
    "taxonomy": "iptc-subjectcode",
    "label": "shot put",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005023"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "04005004",
    "taxonomy": "iptc-subjectcode",
    "label": "oil and gas - upstream activities",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "12009006",
    "taxonomy": "iptc-subjectcode",
    "label": "baptist",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "15051011",
    "taxonomy": "iptc-subjectcode",
    "label": "double trap",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }]
    }, {
    "id": "04016019",
    "taxonomy": "iptc-subjectcode",
    "label": "financing and stock offering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016019"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "12004001",
    "taxonomy": "iptc-subjectcode",
    "label": "christianity-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12004000"
    }]
    }, {
    "id": "08005003",
    "taxonomy": "iptc-subjectcode",
    "label": "funeral",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005000"
    }]
    }, {
    "id": "12014001",
    "taxonomy": "iptc-subjectcode",
    "label": "christmas",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12014000"
    }]
    }, {
    "id": "11028000",
    "taxonomy": "iptc-subjectcode",
    "label": "international organisation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11028000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "04016051",
    "taxonomy": "iptc-subjectcode",
    "label": "stock splits",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016051"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15005063",
    "taxonomy": "iptc-subjectcode",
    "label": "880 yards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005063"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "04008030",
    "taxonomy": "iptc-subjectcode",
    "label": "imports",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008030"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "06006001",
    "taxonomy": "iptc-subjectcode",
    "label": "land resources",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06006000"
    }]
    }, {
    "id": "15028001",
    "taxonomy": "iptc-subjectcode",
    "label": "floor exercise",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "16003004",
    "taxonomy": "iptc-subjectcode",
    "label": "religious conflict",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003000"
    }]
    }, {
    "id": "15005006",
    "taxonomy": "iptc-subjectcode",
    "label": "1500 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15072000",
    "taxonomy": "iptc-subjectcode",
    "label": "wrestling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15023000",
    "taxonomy": "iptc-subjectcode",
    "label": "fencing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15023000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15031002",
    "taxonomy": "iptc-subjectcode",
    "label": "sledge hockey",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15031002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15031000"
    }]
    }, {
    "id": "04008006",
    "taxonomy": "iptc-subjectcode",
    "label": "foreign exchange market",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15005057",
    "taxonomy": "iptc-subjectcode",
    "label": "300 yards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005057"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "07008000",
    "taxonomy": "iptc-subjectcode",
    "label": "preventative medicine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "04007012",
    "taxonomy": "iptc-subjectcode",
    "label": "toy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "15019013",
    "taxonomy": "iptc-subjectcode",
    "label": "staging race",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "17003000",
    "taxonomy": "iptc-subjectcode",
    "label": "report",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17000000"
    }]
    }, {
    "id": "12003000",
    "taxonomy": "iptc-subjectcode",
    "label": "freemasonry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15010006",
    "taxonomy": "iptc-subjectcode",
    "label": "snooker",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15010000"
    }]
    }, {
    "id": "16006001",
    "taxonomy": "iptc-subjectcode",
    "label": "genocide",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16006000"
    }]
    }, {
    "id": "04014000",
    "taxonomy": "iptc-subjectcode",
    "label": "tourism and leisure",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "04016022",
    "taxonomy": "iptc-subjectcode",
    "label": "insider trading",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016022"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "15005046",
    "taxonomy": "iptc-subjectcode",
    "label": "50 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005046"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "14023000",
    "taxonomy": "iptc-subjectcode",
    "label": "death and dying",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14023000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "05005003",
    "taxonomy": "iptc-subjectcode",
    "label": "high schools",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05005003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05005000"
    }]
    }, {
    "id": "10018000",
    "taxonomy": "iptc-subjectcode",
    "label": "wedding",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10018000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "15070006",
    "taxonomy": "iptc-subjectcode",
    "label": "75 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "07001001",
    "taxonomy": "iptc-subjectcode",
    "label": "communicable diseases",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001000"
    }]
    }, {
    "id": "01026002",
    "taxonomy": "iptc-subjectcode",
    "label": "news media",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01026002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01026000"
    }]
    }, {
    "id": "13004000",
    "taxonomy": "iptc-subjectcode",
    "label": "natural science",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "10000000",
    "taxonomy": "iptc-subjectcode",
    "label": "lifestyle and leisure",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "06008000",
    "taxonomy": "iptc-subjectcode",
    "label": "population",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06000000"
    }]
    }, {
    "id": "04008023",
    "taxonomy": "iptc-subjectcode",
    "label": "financial markets",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008023"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15056006",
    "taxonomy": "iptc-subjectcode",
    "label": "10000 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15056000"
    }]
    }, {
    "id": "08001000",
    "taxonomy": "iptc-subjectcode",
    "label": "animal",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08000000"
    }]
    }, {
    "id": "15073045",
    "taxonomy": "iptc-subjectcode",
    "label": "exhibition",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073045"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15025001",
    "taxonomy": "iptc-subjectcode",
    "label": "singles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15025001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15025000"
    }]
    }, {
    "id": "13014000",
    "taxonomy": "iptc-subjectcode",
    "label": "marine science",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "11003004",
    "taxonomy": "iptc-subjectcode",
    "label": "national elections",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }]
    }, {
    "id": "07019000",
    "taxonomy": "iptc-subjectcode",
    "label": "patient",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07019000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "15023003",
    "taxonomy": "iptc-subjectcode",
    "label": "sabre",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15023003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15023000"
    }]
    }, {
    "id": "15062011",
    "taxonomy": "iptc-subjectcode",
    "label": "100 m backstroke",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "16002000",
    "taxonomy": "iptc-subjectcode",
    "label": "armed conflict",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "15050005",
    "taxonomy": "iptc-subjectcode",
    "label": "Laser",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }]
    }, {
    "id": "15073019",
    "taxonomy": "iptc-subjectcode",
    "label": "intercontinental cup",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073019"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15005024",
    "taxonomy": "iptc-subjectcode",
    "label": "discus throw",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005024"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "02008001",
    "taxonomy": "iptc-subjectcode",
    "label": "litigation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02008001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02008000"
    }]
    }, {
    "id": "15030003",
    "taxonomy": "iptc-subjectcode",
    "label": "trotting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15030003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15030000"
    }]
    }, {
    "id": "04007006",
    "taxonomy": "iptc-subjectcode",
    "label": "speciality store",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04007000"
    }]
    }, {
    "id": "07001006",
    "taxonomy": "iptc-subjectcode",
    "label": "alzheimer's disease",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07001000"
    }]
    }, {
    "id": "12022000",
    "taxonomy": "iptc-subjectcode",
    "label": "confucianism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12022000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "04002005",
    "taxonomy": "iptc-subjectcode",
    "label": "organic chemical",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002000"
    }]
    }, {
    "id": "10005000",
    "taxonomy": "iptc-subjectcode",
    "label": "holiday or vacation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "15081000",
    "taxonomy": "iptc-subjectcode",
    "label": "croquette",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15081000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "13004003",
    "taxonomy": "iptc-subjectcode",
    "label": "geography",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13004000"
    }]
    }, {
    "id": "09014000",
    "taxonomy": "iptc-subjectcode",
    "label": "advanced training",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09014000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "15043013",
    "taxonomy": "iptc-subjectcode",
    "label": "nordic combined",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "15005056",
    "taxonomy": "iptc-subjectcode",
    "label": "300 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005056"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15072009",
    "taxonomy": "iptc-subjectcode",
    "label": "63 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "04004007",
    "taxonomy": "iptc-subjectcode",
    "label": "design and engineering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04004000"
    }]
    }, {
    "id": "10007000",
    "taxonomy": "iptc-subjectcode",
    "label": "travel and commuting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "01024000",
    "taxonomy": "iptc-subjectcode",
    "label": "cartoon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01024000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15073044",
    "taxonomy": "iptc-subjectcode",
    "label": "all-stars competition",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073044"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "09002001",
    "taxonomy": "iptc-subjectcode",
    "label": "contract issue-wages",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09002001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09002000"
    }]
    }, {
    "id": "15074006",
    "taxonomy": "iptc-subjectcode",
    "label": "bareback",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15074000"
    }]
    }, {
    "id": "04017001",
    "taxonomy": "iptc-subjectcode",
    "label": "economic policy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04017001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04017000"
    }]
    }, {
    "id": "03006001",
    "taxonomy": "iptc-subjectcode",
    "label": "structural failures",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03006000"
    }]
    }, {
    "id": "10004002",
    "taxonomy": "iptc-subjectcode",
    "label": "shopping",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10004002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10004000"
    }]
    }, {
    "id": "15047004",
    "taxonomy": "iptc-subjectcode",
    "label": "coxless pair",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15047000"
    }]
    }, {
    "id": "15050000",
    "taxonomy": "iptc-subjectcode",
    "label": "sailing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15050000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15073012",
    "taxonomy": "iptc-subjectcode",
    "label": "SouthEast Asiatic Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15005045",
    "taxonomy": "iptc-subjectcode",
    "label": "3000 m walk",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005045"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15022002",
    "taxonomy": "iptc-subjectcode",
    "label": "dressage",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15022002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15022000"
    }]
    }, {
    "id": "15028002",
    "taxonomy": "iptc-subjectcode",
    "label": "vault",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "16009000",
    "taxonomy": "iptc-subjectcode",
    "label": "war",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "15062007",
    "taxonomy": "iptc-subjectcode",
    "label": "relay 4x50 m freestyle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "05008000",
    "taxonomy": "iptc-subjectcode",
    "label": "upbringing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05008000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "15014018",
    "taxonomy": "iptc-subjectcode",
    "label": "straw",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014018"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "01003000",
    "taxonomy": "iptc-subjectcode",
    "label": "bullfighting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "11015000",
    "taxonomy": "iptc-subjectcode",
    "label": "constitution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "04009002",
    "taxonomy": "iptc-subjectcode",
    "label": "metal",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04009002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04009000"
    }]
    }, {
    "id": "15005039",
    "taxonomy": "iptc-subjectcode",
    "label": "50 km walk",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005039"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "01011002",
    "taxonomy": "iptc-subjectcode",
    "label": "folk music",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01011000"
    }]
    }, {
    "id": "09002002",
    "taxonomy": "iptc-subjectcode",
    "label": "contract issue-healthcare",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09002002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09002000"
    }]
    }, {
    "id": "02012006",
    "taxonomy": "iptc-subjectcode",
    "label": "corruption",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02012000"
    }]
    }, {
    "id": "11003010",
    "taxonomy": "iptc-subjectcode",
    "label": "primary",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11003000"
    }]
    }, {
    "id": "16000000",
    "taxonomy": "iptc-subjectcode",
    "label": "unrest, conflicts and war",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16000000"
    }]
    }, {
    "id": "04008034",
    "taxonomy": "iptc-subjectcode",
    "label": "business enterprises",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008034"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15032010",
    "taxonomy": "iptc-subjectcode",
    "label": "pala-corta",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "04002007",
    "taxonomy": "iptc-subjectcode",
    "label": "synthetic and plastic",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002000"
    }]
    }, {
    "id": "15072004",
    "taxonomy": "iptc-subjectcode",
    "label": "130 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15072000"
    }]
    }, {
    "id": "15039004",
    "taxonomy": "iptc-subjectcode",
    "label": "Indy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15039000"
    }]
    }, {
    "id": "12023002",
    "taxonomy": "iptc-subjectcode",
    "label": "qur'an",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12023002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12023000"
    }]
    }, {
    "id": "04011000",
    "taxonomy": "iptc-subjectcode",
    "label": "manufacturing and engineering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "14027000",
    "taxonomy": "iptc-subjectcode",
    "label": "reconstruction",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14027000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15004000",
    "taxonomy": "iptc-subjectcode",
    "label": "archery",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "04015002",
    "taxonomy": "iptc-subjectcode",
    "label": "railway",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04015002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04015000"
    }]
    }, {
    "id": "15070014",
    "taxonomy": "iptc-subjectcode",
    "label": "105 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "12020000",
    "taxonomy": "iptc-subjectcode",
    "label": "jainism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12020000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12000000"
    }]
    }, {
    "id": "15073001",
    "taxonomy": "iptc-subjectcode",
    "label": "Summer Olympics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "03011000",
    "taxonomy": "iptc-subjectcode",
    "label": "volcanic eruption",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/03000000"
    }]
    }, {
    "id": "07010000",
    "taxonomy": "iptc-subjectcode",
    "label": "hospital and clinic",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07010000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "10015000",
    "taxonomy": "iptc-subjectcode",
    "label": "adventure",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10015000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "15030000",
    "taxonomy": "iptc-subjectcode",
    "label": "horse racing, harness racing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15030000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15016001",
    "taxonomy": "iptc-subjectcode",
    "label": "mountaineering",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15016001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15016000"
    }]
    }, {
    "id": "15028013",
    "taxonomy": "iptc-subjectcode",
    "label": "rope",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "15073040",
    "taxonomy": "iptc-subjectcode",
    "label": "national tournament",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073040"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15005067",
    "taxonomy": "iptc-subjectcode",
    "label": "6 miles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005067"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "05010002",
    "taxonomy": "iptc-subjectcode",
    "label": "teachers",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05010002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05010000"
    }]
    }, {
    "id": "15051000",
    "taxonomy": "iptc-subjectcode",
    "label": "shooting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15051000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "17001000",
    "taxonomy": "iptc-subjectcode",
    "label": "forecast",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17001000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/17000000"
    }]
    }, {
    "id": "09009000",
    "taxonomy": "iptc-subjectcode",
    "label": "unemployment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09009000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09000000"
    }]
    }, {
    "id": "11001007",
    "taxonomy": "iptc-subjectcode",
    "label": "biological and chemical weapons",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11001000"
    }]
    }, {
    "id": "15036000",
    "taxonomy": "iptc-subjectcode",
    "label": "luge",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15036000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "01010002",
    "taxonomy": "iptc-subjectcode",
    "label": "poetry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01010002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01010000"
    }]
    }, {
    "id": "15032006",
    "taxonomy": "iptc-subjectcode",
    "label": "chistera ancha",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }]
    }, {
    "id": "15028012",
    "taxonomy": "iptc-subjectcode",
    "label": "ribbon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028012"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "15015007",
    "taxonomy": "iptc-subjectcode",
    "label": "K4",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015007"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "14025001",
    "taxonomy": "iptc-subjectcode",
    "label": "social conditions",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14025000"
    }]
    }, {
    "id": "14013000",
    "taxonomy": "iptc-subjectcode",
    "label": "prostitution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "04008031",
    "taxonomy": "iptc-subjectcode",
    "label": "exports",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008031"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "04006009",
    "taxonomy": "iptc-subjectcode",
    "label": "stock broking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15021003",
    "taxonomy": "iptc-subjectcode",
    "label": "3 m springboard",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15021000"
    }]
    }, {
    "id": "02003001",
    "taxonomy": "iptc-subjectcode",
    "label": "law enforcement",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02003000"
    }]
    }, {
    "id": "10013000",
    "taxonomy": "iptc-subjectcode",
    "label": "fishing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/10000000"
    }]
    }, {
    "id": "13007000",
    "taxonomy": "iptc-subjectcode",
    "label": "scientific exploration",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13007000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "15028006",
    "taxonomy": "iptc-subjectcode",
    "label": "horizontal bar",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15028000"
    }]
    }, {
    "id": "15005034",
    "taxonomy": "iptc-subjectcode",
    "label": "walk 2 h",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005034"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "04003002",
    "taxonomy": "iptc-subjectcode",
    "label": "networking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003000"
    }]
    }, {
    "id": "04001004",
    "taxonomy": "iptc-subjectcode",
    "label": "livestock farming",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04001000"
    }]
    }, {
    "id": "12009002",
    "taxonomy": "iptc-subjectcode",
    "label": "lutheran",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "07011000",
    "taxonomy": "iptc-subjectcode",
    "label": "government health care",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07011000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "12025001",
    "taxonomy": "iptc-subjectcode",
    "label": "catholic convention",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12025001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12025000"
    }]
    }, {
    "id": "13003004",
    "taxonomy": "iptc-subjectcode",
    "label": "sociology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13003000"
    }]
    }, {
    "id": "04016054",
    "taxonomy": "iptc-subjectcode",
    "label": "globalization",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016054"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "04008028",
    "taxonomy": "iptc-subjectcode",
    "label": "mutual funds",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008028"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "11006009",
    "taxonomy": "iptc-subjectcode",
    "label": "ministers (government)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006009"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "15052000",
    "taxonomy": "iptc-subjectcode",
    "label": "ski jumping",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15052000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15019015",
    "taxonomy": "iptc-subjectcode",
    "label": "Vtt",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019015"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "04008003",
    "taxonomy": "iptc-subjectcode",
    "label": "debt market",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04008000"
    }]
    }, {
    "id": "15073008",
    "taxonomy": "iptc-subjectcode",
    "label": "Winter Asian Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15077003",
    "taxonomy": "iptc-subjectcode",
    "label": "overall",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }]
    }, {
    "id": "04002004",
    "taxonomy": "iptc-subjectcode",
    "label": "inorganic chemical",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04002000"
    }]
    }, {
    "id": "14010001",
    "taxonomy": "iptc-subjectcode",
    "label": "gays and lesbians",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14010001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14010000"
    }]
    }, {
    "id": "07012000",
    "taxonomy": "iptc-subjectcode",
    "label": "private health care",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07012000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "15053001",
    "taxonomy": "iptc-subjectcode",
    "label": "giant slalom",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15053001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15053000"
    }]
    }, {
    "id": "14006005",
    "taxonomy": "iptc-subjectcode",
    "label": "sex",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006000"
    }]
    }, {
    "id": "08005000",
    "taxonomy": "iptc-subjectcode",
    "label": "society",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08000000"
    }]
    }, {
    "id": "15005020",
    "taxonomy": "iptc-subjectcode",
    "label": "pole vault",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005020"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "15041013",
    "taxonomy": "iptc-subjectcode",
    "label": "side-cars",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041013"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "02001002",
    "taxonomy": "iptc-subjectcode",
    "label": "computer crime",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02001000"
    }]
    }, {
    "id": "07003001",
    "taxonomy": "iptc-subjectcode",
    "label": "prescription drugs",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07003000"
    }]
    }, {
    "id": "15032000",
    "taxonomy": "iptc-subjectcode",
    "label": "Jai Alai (Pelota)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15032000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "01019000",
    "taxonomy": "iptc-subjectcode",
    "label": "customs and tradition",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01019000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "11009002",
    "taxonomy": "iptc-subjectcode",
    "label": "lower house",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11009002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11009000"
    }]
    }, {
    "id": "15015003",
    "taxonomy": "iptc-subjectcode",
    "label": "500 m",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15015000"
    }]
    }, {
    "id": "15043002",
    "taxonomy": "iptc-subjectcode",
    "label": "5 km classical time",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15043000"
    }]
    }, {
    "id": "04005008",
    "taxonomy": "iptc-subjectcode",
    "label": "water supply",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005008"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04005000"
    }]
    }, {
    "id": "14002000",
    "taxonomy": "iptc-subjectcode",
    "label": "charity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14002000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "08006000",
    "taxonomy": "iptc-subjectcode",
    "label": "award and prize",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08000000"
    }]
    }, {
    "id": "15066002",
    "taxonomy": "iptc-subjectcode",
    "label": "triathlon cycling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15066002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15066000"
    }]
    }, {
    "id": "04012004",
    "taxonomy": "iptc-subjectcode",
    "label": "non ferrous metal",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04012000"
    }]
    }, {
    "id": "15058003",
    "taxonomy": "iptc-subjectcode",
    "label": "continental federation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15058000"
    }]
    }, {
    "id": "09011002",
    "taxonomy": "iptc-subjectcode",
    "label": "social security",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09011002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/09011000"
    }]
    }, {
    "id": "05005000",
    "taxonomy": "iptc-subjectcode",
    "label": "school",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/05000000"
    }]
    }, {
    "id": "06007001",
    "taxonomy": "iptc-subjectcode",
    "label": "invasive species",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06007001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06007000"
    }]
    }, {
    "id": "15073016",
    "taxonomy": "iptc-subjectcode",
    "label": "Summer Goodwill Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073016"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15038003",
    "taxonomy": "iptc-subjectcode",
    "label": "swimming",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15038000"
    }]
    }, {
    "id": "15003003",
    "taxonomy": "iptc-subjectcode",
    "label": "AFL-DEPRECATED",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15003003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15003000"
    }]
    }, {
    "id": "11013000",
    "taxonomy": "iptc-subjectcode",
    "label": "state budget and tax",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11013000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "14024001",
    "taxonomy": "iptc-subjectcode",
    "label": "children",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14024000"
    }]
    }, {
    "id": "15093000",
    "taxonomy": "iptc-subjectcode",
    "label": "kendo",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15093000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "11016000",
    "taxonomy": "iptc-subjectcode",
    "label": "interior policy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "12009010",
    "taxonomy": "iptc-subjectcode",
    "label": "roman catholic",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/12009000"
    }]
    }, {
    "id": "01025000",
    "taxonomy": "iptc-subjectcode",
    "label": "animation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01025000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "13010001",
    "taxonomy": "iptc-subjectcode",
    "label": "rocketry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13010001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13010000"
    }]
    }, {
    "id": "04003006",
    "taxonomy": "iptc-subjectcode",
    "label": "telecommunication equipment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04003000"
    }]
    }, {
    "id": "14004000",
    "taxonomy": "iptc-subjectcode",
    "label": "disabled",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14004000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15077010",
    "taxonomy": "iptc-subjectcode",
    "label": "disc golf",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077010"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15077000"
    }]
    }, {
    "id": "15069003",
    "taxonomy": "iptc-subjectcode",
    "label": "jump",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15069003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15069000"
    }]
    }, {
    "id": "14003002",
    "taxonomy": "iptc-subjectcode",
    "label": "immigration",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14003002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14003000"
    }]
    }, {
    "id": "15014006",
    "taxonomy": "iptc-subjectcode",
    "label": "middleweight",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15014000"
    }]
    }, {
    "id": "15009005",
    "taxonomy": "iptc-subjectcode",
    "label": "4x7.5 km relay",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15009000"
    }]
    }, {
    "id": "15019020",
    "taxonomy": "iptc-subjectcode",
    "label": "artistic cycling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019020"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15019000"
    }]
    }, {
    "id": "13006000",
    "taxonomy": "iptc-subjectcode",
    "label": "research",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13006000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "01026001",
    "taxonomy": "iptc-subjectcode",
    "label": "periodicals",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01026001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01026000"
    }]
    }, {
    "id": "13001002",
    "taxonomy": "iptc-subjectcode",
    "label": "chemistry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13001002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13001000"
    }]
    }, {
    "id": "04018001",
    "taxonomy": "iptc-subjectcode",
    "label": "institution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04018001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04018000"
    }]
    }, {
    "id": "01017000",
    "taxonomy": "iptc-subjectcode",
    "label": "theatre",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01017000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "15073005",
    "taxonomy": "iptc-subjectcode",
    "label": "Commonwealth Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15073000"
    }]
    }, {
    "id": "15071003",
    "taxonomy": "iptc-subjectcode",
    "label": "river",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15071003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15071000"
    }]
    }, {
    "id": "15005060",
    "taxonomy": "iptc-subjectcode",
    "label": "500 yards",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005060"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15005000"
    }]
    }, {
    "id": "08003000",
    "taxonomy": "iptc-subjectcode",
    "label": "people",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08003000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/08000000"
    }]
    }, {
    "id": "07017000",
    "taxonomy": "iptc-subjectcode",
    "label": "illness",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07017000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/07000000"
    }]
    }, {
    "id": "15070003",
    "taxonomy": "iptc-subjectcode",
    "label": "48 kg",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070003"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15070000"
    }]
    }, {
    "id": "11006005",
    "taxonomy": "iptc-subjectcode",
    "label": "executive (government)",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11006000"
    }]
    }, {
    "id": "04016011",
    "taxonomy": "iptc-subjectcode",
    "label": "corporate officer",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016011"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }]
    }, {
    "id": "14020000",
    "taxonomy": "iptc-subjectcode",
    "label": "nuclear radiation victims",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14020000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14000000"
    }]
    }, {
    "id": "15048000",
    "taxonomy": "iptc-subjectcode",
    "label": "rugby league",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15048000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "13005000",
    "taxonomy": "iptc-subjectcode",
    "label": "philosophical science",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13005000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/13000000"
    }]
    }, {
    "id": "15062014",
    "taxonomy": "iptc-subjectcode",
    "label": "100 m breaststroke",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062014"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "06005001",
    "taxonomy": "iptc-subjectcode",
    "label": "air pollution",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06005001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/06005000"
    }]
    }, {
    "id": "16003005",
    "taxonomy": "iptc-subjectcode",
    "label": "social conflict",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/16003000"
    }]
    }, {
    "id": "11022000",
    "taxonomy": "iptc-subjectcode",
    "label": "regulatory policy and organisation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11022000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "01028000",
    "taxonomy": "iptc-subjectcode",
    "label": "history",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01028000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/01000000"
    }]
    }, {
    "id": "11020000",
    "taxonomy": "iptc-subjectcode",
    "label": "nuclear policy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11020000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/11000000"
    }]
    }, {
    "id": "04006005",
    "taxonomy": "iptc-subjectcode",
    "label": "healthcare provider",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04006000"
    }]
    }, {
    "id": "15041006",
    "taxonomy": "iptc-subjectcode",
    "label": "rallying",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041006"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15041000"
    }]
    }, {
    "id": "02002002",
    "taxonomy": "iptc-subjectcode",
    "label": "judge",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02002002"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/02002000"
    }]
    }, {
    "id": "04016000",
    "taxonomy": "iptc-subjectcode",
    "label": "company information",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04016000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04000000"
    }]
    }, {
    "id": "15033000",
    "taxonomy": "iptc-subjectcode",
    "label": "judo",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15033000"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15000000"
    }]
    }, {
    "id": "15002004",
    "taxonomy": "iptc-subjectcode",
    "label": "slalom",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002004"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15002000"
    }]
    }, {
    "id": "15062025",
    "taxonomy": "iptc-subjectcode",
    "label": "synchronised technical routine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062025"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/15062000"
    }]
    }, {
    "id": "04013005",
    "taxonomy": "iptc-subjectcode",
    "label": "rubber product",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013005"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/04013000"
    }]
    }, {
    "id": "14006001",
    "taxonomy": "iptc-subjectcode",
    "label": "parent and child",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006001"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iptc-subjectcode/14006000"
    }]
    }]
    iab = [{
    "id": "IAB7-43",
    "taxonomy": "iab-qag",
    "label": "Thyroid Disease",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-43"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB2-13",
    "taxonomy": "iab-qag",
    "label": "Luxury",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-13"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB8-18",
    "taxonomy": "iab-qag",
    "label": "Wine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-18"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB21-1",
    "taxonomy": "iab-qag",
    "label": "Apartments",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB21-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB21"
    }]
    }, {
    "id": "IAB15-2",
    "taxonomy": "iab-qag",
    "label": "Biology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }, {
    "id": "IAB5-3",
    "taxonomy": "iab-qag",
    "label": "Art History",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB20-9",
    "taxonomy": "iab-qag",
    "label": "Camping",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB8-10",
    "taxonomy": "iab-qag",
    "label": "Food Allergies",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB14-8",
    "taxonomy": "iab-qag",
    "label": "Ethnic Specific",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14"
    }]
    }, {
    "id": "IAB23-2",
    "taxonomy": "iab-qag",
    "label": "Atheism/Agnosticism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB2-15",
    "taxonomy": "iab-qag",
    "label": "Motorcycles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-15"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB7-9",
    "taxonomy": "iab-qag",
    "label": "Bipolar Disorder",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB19-22",
    "taxonomy": "iab-qag",
    "label": "MP3/MIDI",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-22"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB7-21",
    "taxonomy": "iab-qag",
    "label": "Epilepsy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-21"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB19-13",
    "taxonomy": "iab-qag",
    "label": "Desktop Publishing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-13"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB2-8",
    "taxonomy": "iab-qag",
    "label": "Crossover",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB25-2",
    "taxonomy": "iab-qag",
    "label": "Extreme Graphic/Explicit Violence",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25"
    }]
    }, {
    "id": "IAB19-4",
    "taxonomy": "iab-qag",
    "label": "C/C++",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB7-10",
    "taxonomy": "iab-qag",
    "label": "Brain Tumor",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB9-26",
    "taxonomy": "iab-qag",
    "label": "Sci-Fi & Fantasy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-26"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB13-7",
    "taxonomy": "iab-qag",
    "label": "Investing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB4-10",
    "taxonomy": "iab-qag",
    "label": "U.S. Military",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB20-24",
    "taxonomy": "iab-qag",
    "label": "Spas",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-24"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB9-18",
    "taxonomy": "iab-qag",
    "label": "Investors & Patents",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-18"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB11-3",
    "taxonomy": "iab-qag",
    "label": "U.S. Government Resources",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11"
    }]
    }, {
    "id": "IAB7-29",
    "taxonomy": "iab-qag",
    "label": "Incontinence",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-29"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB20-4",
    "taxonomy": "iab-qag",
    "label": "Australia & New Zealand",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB23-7",
    "taxonomy": "iab-qag",
    "label": "Islam",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB8-8",
    "taxonomy": "iab-qag",
    "label": "Desserts & Baking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB25-7",
    "taxonomy": "iab-qag",
    "label": "Incentivized",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25"
    }]
    }, {
    "id": "IAB7-6",
    "taxonomy": "iab-qag",
    "label": "Arthritis",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB26-3",
    "taxonomy": "iab-qag",
    "label": "Spyware/Malware",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB26-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB26"
    }]
    }, {
    "id": "IAB10-8",
    "taxonomy": "iab-qag",
    "label": "Landscaping",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10"
    }]
    }, {
    "id": "IAB20-10",
    "taxonomy": "iab-qag",
    "label": "Canada",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB6-5",
    "taxonomy": "iab-qag",
    "label": "Parenting - K-6 Kids",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6"
    }]
    }, {
    "id": "IAB11-4",
    "taxonomy": "iab-qag",
    "label": "Politics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11"
    }]
    }, {
    "id": "IAB9-29",
    "taxonomy": "iab-qag",
    "label": "Stamps & Coins",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-29"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB19-33",
    "taxonomy": "iab-qag",
    "label": "Web Clip Art",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-33"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB17-5",
    "taxonomy": "iab-qag",
    "label": "Boxing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB9",
    "taxonomy": "iab-qag",
    "label": "Hobbies & Interests",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB5-9",
    "taxonomy": "iab-qag",
    "label": "Graduate School",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB15-6",
    "taxonomy": "iab-qag",
    "label": "Physics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }, {
    "id": "IAB19-26",
    "taxonomy": "iab-qag",
    "label": "Palmtops/PDAs",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-26"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB20-21",
    "taxonomy": "iab-qag",
    "label": "Mexico & Central America",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-21"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB14-4",
    "taxonomy": "iab-qag",
    "label": "Marriage",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14"
    }]
    }, {
    "id": "IAB2-4",
    "taxonomy": "iab-qag",
    "label": "Car Culture",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB17-41",
    "taxonomy": "iab-qag",
    "label": "Volleyball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-41"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB8-7",
    "taxonomy": "iab-qag",
    "label": "Cuisine-Specific",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB13-3",
    "taxonomy": "iab-qag",
    "label": "Financial News",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB9-1",
    "taxonomy": "iab-qag",
    "label": "Art/Technology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB7-2",
    "taxonomy": "iab-qag",
    "label": "A.D.D.",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB23-3",
    "taxonomy": "iab-qag",
    "label": "Buddhism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB17-30",
    "taxonomy": "iab-qag",
    "label": "Running/Jogging",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-30"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB8-15",
    "taxonomy": "iab-qag",
    "label": "Mexican Cuisine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-15"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB17-6",
    "taxonomy": "iab-qag",
    "label": "Canoeing/Kayaking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB3-6",
    "taxonomy": "iab-qag",
    "label": "Forestry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB5-13",
    "taxonomy": "iab-qag",
    "label": "Private School",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-13"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB24",
    "taxonomy": "iab-qag",
    "label": "Uncategorized",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB24"
    }]
    }, {
    "id": "IAB7-39",
    "taxonomy": "iab-qag",
    "label": "Sexuality",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-39"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB7-20",
    "taxonomy": "iab-qag",
    "label": "Diabetes",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-20"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB7-18",
    "taxonomy": "iab-qag",
    "label": "Depression",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-18"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB9-8",
    "taxonomy": "iab-qag",
    "label": "Chess",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB2-5",
    "taxonomy": "iab-qag",
    "label": "Certified Pre-Owned",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB20-27",
    "taxonomy": "iab-qag",
    "label": "United Kingdom",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-27"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB9-22",
    "taxonomy": "iab-qag",
    "label": "Painting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-22"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB8-3",
    "taxonomy": "iab-qag",
    "label": "Cajun/Creole",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB16-2",
    "taxonomy": "iab-qag",
    "label": "Birds",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16"
    }]
    }, {
    "id": "IAB4-5",
    "taxonomy": "iab-qag",
    "label": "Job Search",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB6",
    "taxonomy": "iab-qag",
    "label": "Family & Parenting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6"
    }]
    }, {
    "id": "IAB9-5",
    "taxonomy": "iab-qag",
    "label": "Board Games/Puzzles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB17-22",
    "taxonomy": "iab-qag",
    "label": "NASCAR Racing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-22"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB3-10",
    "taxonomy": "iab-qag",
    "label": "Logistics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB17-34",
    "taxonomy": "iab-qag",
    "label": "Skateboarding",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-34"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB3-2",
    "taxonomy": "iab-qag",
    "label": "Agriculture",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB7-14",
    "taxonomy": "iab-qag",
    "label": "Chronic Pain",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-14"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB17-11",
    "taxonomy": "iab-qag",
    "label": "Fly Fishing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB17-17",
    "taxonomy": "iab-qag",
    "label": "Horses",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-17"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB9-12",
    "taxonomy": "iab-qag",
    "label": "Drawing/Sketching",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-12"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB5-2",
    "taxonomy": "iab-qag",
    "label": "Adult Education",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB19-3",
    "taxonomy": "iab-qag",
    "label": "Antivirus Software",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB15-9",
    "taxonomy": "iab-qag",
    "label": "Botany",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }, {
    "id": "IAB7-35",
    "taxonomy": "iab-qag",
    "label": "Pediatrics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-35"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB1-5",
    "taxonomy": "iab-qag",
    "label": "Movies",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1"
    }]
    }, {
    "id": "IAB19",
    "taxonomy": "iab-qag",
    "label": "Technology & Computing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB20-16",
    "taxonomy": "iab-qag",
    "label": "Greece",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-16"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB4-7",
    "taxonomy": "iab-qag",
    "label": "Nursing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB20-13",
    "taxonomy": "iab-qag",
    "label": "Eastern Europe",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-13"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB19-16",
    "taxonomy": "iab-qag",
    "label": "Graphics Software",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-16"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB7-33",
    "taxonomy": "iab-qag",
    "label": "Orthopedics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-33"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB9-11",
    "taxonomy": "iab-qag",
    "label": "Comic Books",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB5-7",
    "taxonomy": "iab-qag",
    "label": "English as a 2nd Language",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB2-20",
    "taxonomy": "iab-qag",
    "label": "Sedan",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-20"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB2-19",
    "taxonomy": "iab-qag",
    "label": "Road-Side Assistance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-19"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB17-4",
    "taxonomy": "iab-qag",
    "label": "Bodybuilding",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB19-9",
    "taxonomy": "iab-qag",
    "label": "Computer Peripherals",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB13",
    "taxonomy": "iab-qag",
    "label": "Personal Finance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB9-23",
    "taxonomy": "iab-qag",
    "label": "Photography",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-23"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB13-10",
    "taxonomy": "iab-qag",
    "label": "Retirement Planning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB25-6",
    "taxonomy": "iab-qag",
    "label": "Under Construction",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25"
    }]
    }, {
    "id": "IAB9-14",
    "taxonomy": "iab-qag",
    "label": "Genealogy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-14"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB7-25",
    "taxonomy": "iab-qag",
    "label": "Herbs for Health",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-25"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB17-28",
    "taxonomy": "iab-qag",
    "label": "Rodeo",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-28"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB17-42",
    "taxonomy": "iab-qag",
    "label": "Walking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-42"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB8-4",
    "taxonomy": "iab-qag",
    "label": "Chinese Cuisine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB11-5",
    "taxonomy": "iab-qag",
    "label": "Commentary",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11"
    }]
    }, {
    "id": "IAB17-37",
    "taxonomy": "iab-qag",
    "label": "Surfing/Bodyboarding",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-37"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB15-5",
    "taxonomy": "iab-qag",
    "label": "Paranormal Phenomena",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }, {
    "id": "IAB17-21",
    "taxonomy": "iab-qag",
    "label": "Mountain Biking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-21"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB8-1",
    "taxonomy": "iab-qag",
    "label": "American Cuisine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB22-4",
    "taxonomy": "iab-qag",
    "label": "Engines",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB22-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB22"
    }]
    }, {
    "id": "IAB4-3",
    "taxonomy": "iab-qag",
    "label": "Financial Aid",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB4",
    "taxonomy": "iab-qag",
    "label": "Careers",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB23-1",
    "taxonomy": "iab-qag",
    "label": "Alternative Religions",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB14-7",
    "taxonomy": "iab-qag",
    "label": "Weddings",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14"
    }]
    }, {
    "id": "IAB13-1",
    "taxonomy": "iab-qag",
    "label": "Beginning Investing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB17-1",
    "taxonomy": "iab-qag",
    "label": "Auto Racing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB7-44",
    "taxonomy": "iab-qag",
    "label": "Weight Loss",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-44"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB9-25",
    "taxonomy": "iab-qag",
    "label": "Roleplaying Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-25"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB6-2",
    "taxonomy": "iab-qag",
    "label": "Babies & Toddlers",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6"
    }]
    }, {
    "id": "IAB13-6",
    "taxonomy": "iab-qag",
    "label": "Insurance",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB17-10",
    "taxonomy": "iab-qag",
    "label": "Figure Skating",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB10-2",
    "taxonomy": "iab-qag",
    "label": "Entertaining",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10"
    }]
    }, {
    "id": "IAB19-32",
    "taxonomy": "iab-qag",
    "label": "Visual Basic",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-32"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB1-7",
    "taxonomy": "iab-qag",
    "label": "Television",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1"
    }]
    }, {
    "id": "IAB11-2",
    "taxonomy": "iab-qag",
    "label": "Legal Issues",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11"
    }]
    }, {
    "id": "IAB19-25",
    "taxonomy": "iab-qag",
    "label": "Network Security",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-25"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB2-16",
    "taxonomy": "iab-qag",
    "label": "Off-Road Vehicles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-16"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB17",
    "taxonomy": "iab-qag",
    "label": "Sports",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB2-7",
    "taxonomy": "iab-qag",
    "label": "Coupe",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB15-1",
    "taxonomy": "iab-qag",
    "label": "Astrology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }, {
    "id": "IAB8",
    "taxonomy": "iab-qag",
    "label": "Food & Drink",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB13-12",
    "taxonomy": "iab-qag",
    "label": "Tax Planning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-12"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB17-35",
    "taxonomy": "iab-qag",
    "label": "Skiing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-35"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB3-9",
    "taxonomy": "iab-qag",
    "label": "Human Resources",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB23-8",
    "taxonomy": "iab-qag",
    "label": "Judaism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB19-30",
    "taxonomy": "iab-qag",
    "label": "Shareware/Freeware",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-30"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB14-3",
    "taxonomy": "iab-qag",
    "label": "Gay Life",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14"
    }]
    }, {
    "id": "IAB6-8",
    "taxonomy": "iab-qag",
    "label": "Special Needs Kids",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6"
    }]
    }, {
    "id": "IAB20-20",
    "taxonomy": "iab-qag",
    "label": "Japan",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-20"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB6-6",
    "taxonomy": "iab-qag",
    "label": "Parenting teens",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6"
    }]
    }, {
    "id": "IAB9-30",
    "taxonomy": "iab-qag",
    "label": "Video & Computer Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-30"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB13-2",
    "taxonomy": "iab-qag",
    "label": "Credit/Debt & Loans",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB20-6",
    "taxonomy": "iab-qag",
    "label": "Budget Travel",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB20-23",
    "taxonomy": "iab-qag",
    "label": "South America",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-23"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB19-36",
    "taxonomy": "iab-qag",
    "label": "Windows",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-36"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB16-6",
    "taxonomy": "iab-qag",
    "label": "Reptiles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16"
    }]
    }, {
    "id": "IAB19-21",
    "taxonomy": "iab-qag",
    "label": "Mac Support",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-21"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB5-4",
    "taxonomy": "iab-qag",
    "label": "College Administration",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB2-23",
    "taxonomy": "iab-qag",
    "label": "Wagon",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-23"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB26-2",
    "taxonomy": "iab-qag",
    "label": "Warez",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB26-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB26"
    }]
    }, {
    "id": "IAB18-5",
    "taxonomy": "iab-qag",
    "label": "Clothing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18"
    }]
    }, {
    "id": "IAB2-12",
    "taxonomy": "iab-qag",
    "label": "Hybrid",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-12"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB7-38",
    "taxonomy": "iab-qag",
    "label": "Senor Health",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-38"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB5",
    "taxonomy": "iab-qag",
    "label": "Education",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB16-7",
    "taxonomy": "iab-qag",
    "label": "Veterinary Medicine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16"
    }]
    }, {
    "id": "IAB7-3",
    "taxonomy": "iab-qag",
    "label": "AIDS/HIV",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB17-31",
    "taxonomy": "iab-qag",
    "label": "Sailing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-31"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB23-4",
    "taxonomy": "iab-qag",
    "label": "Catholicism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB1-1",
    "taxonomy": "iab-qag",
    "label": "Books & Literature",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1"
    }]
    }, {
    "id": "IAB20-12",
    "taxonomy": "iab-qag",
    "label": "Cruises",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-12"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB17-9",
    "taxonomy": "iab-qag",
    "label": "Cricket",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB12",
    "taxonomy": "iab-qag",
    "label": "News",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB12"
    }]
    }, {
    "id": "IAB16-1",
    "taxonomy": "iab-qag",
    "label": "Aquariums",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16"
    }]
    }, {
    "id": "IAB20-17",
    "taxonomy": "iab-qag",
    "label": "Honeymoons/Getaways",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-17"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB7-19",
    "taxonomy": "iab-qag",
    "label": "Dermatology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-19"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB17-29",
    "taxonomy": "iab-qag",
    "label": "Rugby",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-29"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB18-2",
    "taxonomy": "iab-qag",
    "label": "Body Art",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18"
    }]
    }, {
    "id": "IAB9-17",
    "taxonomy": "iab-qag",
    "label": "Home Recording",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-17"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB25-5",
    "taxonomy": "iab-qag",
    "label": "Hate Content",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25"
    }]
    }, {
    "id": "IAB3-3",
    "taxonomy": "iab-qag",
    "label": "Biotech/Biomedical",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB8-16",
    "taxonomy": "iab-qag",
    "label": "Vegan",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-16"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB17-18",
    "taxonomy": "iab-qag",
    "label": "Hunting/Shooting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-18"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB2-22",
    "taxonomy": "iab-qag",
    "label": "Vintage Cars",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-22"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB23",
    "taxonomy": "iab-qag",
    "label": "Religion & Spirituality",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB17-36",
    "taxonomy": "iab-qag",
    "label": "Snowboarding",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-36"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB10-9",
    "taxonomy": "iab-qag",
    "label": "Remodeling & Construction",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10"
    }]
    }, {
    "id": "IAB9-24",
    "taxonomy": "iab-qag",
    "label": "Radio",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-24"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB4-4",
    "taxonomy": "iab-qag",
    "label": "Job Fairs",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB7-34",
    "taxonomy": "iab-qag",
    "label": "Panic/Anxiety Disorders",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-34"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB1",
    "taxonomy": "iab-qag",
    "label": "Arts & Entertainment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1"
    }]
    }, {
    "id": "IAB20",
    "taxonomy": "iab-qag",
    "label": "Travel",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB1-6",
    "taxonomy": "iab-qag",
    "label": "Music",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1"
    }]
    }, {
    "id": "IAB7-15",
    "taxonomy": "iab-qag",
    "label": "Cold & Flu",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-15"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB7-26",
    "taxonomy": "iab-qag",
    "label": "Holistic Healing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-26"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB7-7",
    "taxonomy": "iab-qag",
    "label": "Asthma",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB9-13",
    "taxonomy": "iab-qag",
    "label": "Freelance Writing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-13"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB22-1",
    "taxonomy": "iab-qag",
    "label": "Contests & Freebies",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB22-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB22"
    }]
    }, {
    "id": "IAB19-12",
    "taxonomy": "iab-qag",
    "label": "Databases",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-12"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB25-1",
    "taxonomy": "iab-qag",
    "label": "Unmoderated UGC",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25"
    }]
    }, {
    "id": "IAB7-40",
    "taxonomy": "iab-qag",
    "label": "Sleep Disorders",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-40"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB2-1",
    "taxonomy": "iab-qag",
    "label": "Auto Parts",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB16",
    "taxonomy": "iab-qag",
    "label": "Pets",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16"
    }]
    }, {
    "id": "IAB19-28",
    "taxonomy": "iab-qag",
    "label": "Portable",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-28"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB23-9",
    "taxonomy": "iab-qag",
    "label": "Latter-Day Saints",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB9-4",
    "taxonomy": "iab-qag",
    "label": "Birdwatching",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB18-6",
    "taxonomy": "iab-qag",
    "label": "Accessories",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18"
    }]
    }, {
    "id": "IAB19-17",
    "taxonomy": "iab-qag",
    "label": "Home Video/DVD",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-17"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB19-8",
    "taxonomy": "iab-qag",
    "label": "Computer Networking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB20-3",
    "taxonomy": "iab-qag",
    "label": "Air Travel",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB5-12",
    "taxonomy": "iab-qag",
    "label": "K-6 Educators",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-12"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB9-9",
    "taxonomy": "iab-qag",
    "label": "Cigars",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB7-45",
    "taxonomy": "iab-qag",
    "label": "Women's Health",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-45"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB19-7",
    "taxonomy": "iab-qag",
    "label": "Computer Certification",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB5-5",
    "taxonomy": "iab-qag",
    "label": "College Life",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB19-24",
    "taxonomy": "iab-qag",
    "label": "Net for Beginners",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-24"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB6-9",
    "taxonomy": "iab-qag",
    "label": "Eldercare",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6"
    }]
    }, {
    "id": "IAB23-10",
    "taxonomy": "iab-qag",
    "label": "Pagan/Wiccan",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB7-30",
    "taxonomy": "iab-qag",
    "label": "Infertility",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-30"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB9-20",
    "taxonomy": "iab-qag",
    "label": "Magic & Illusion",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-20"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB25-4",
    "taxonomy": "iab-qag",
    "label": "Profane Content",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25"
    }]
    }, {
    "id": "IAB2-2",
    "taxonomy": "iab-qag",
    "label": "Auto Repair",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB15",
    "taxonomy": "iab-qag",
    "label": "Science",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }, {
    "id": "IAB19-11",
    "taxonomy": "iab-qag",
    "label": "Data Centers",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB17-43",
    "taxonomy": "iab-qag",
    "label": "Waterski/Wakeboard",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-43"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB17-14",
    "taxonomy": "iab-qag",
    "label": "Game & Fish",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-14"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB7-23",
    "taxonomy": "iab-qag",
    "label": "Headaches/Migraines",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-23"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB20-2",
    "taxonomy": "iab-qag",
    "label": "Africa",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB7-12",
    "taxonomy": "iab-qag",
    "label": "Cholesterol",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-12"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB3",
    "taxonomy": "iab-qag",
    "label": "Business",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB17-8",
    "taxonomy": "iab-qag",
    "label": "Climbing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB22",
    "taxonomy": "iab-qag",
    "label": "Shopping",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB22"
    }]
    }, {
    "id": "IAB7-37",
    "taxonomy": "iab-qag",
    "label": "Psychology/Psychiatry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-37"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB6-3",
    "taxonomy": "iab-qag",
    "label": "Daycare/Pre School",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6"
    }]
    }, {
    "id": "IAB7-41",
    "taxonomy": "iab-qag",
    "label": "Smoking Cessation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-41"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB15-4",
    "taxonomy": "iab-qag",
    "label": "Geology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }, {
    "id": "IAB5-1",
    "taxonomy": "iab-qag",
    "label": "7-12 Education",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB20-7",
    "taxonomy": "iab-qag",
    "label": "Business Travel",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB10-1",
    "taxonomy": "iab-qag",
    "label": "Appliances",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10"
    }]
    }, {
    "id": "IAB21-3",
    "taxonomy": "iab-qag",
    "label": "Buying/Selling Homes",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB21-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB21"
    }]
    }, {
    "id": "IAB19-31",
    "taxonomy": "iab-qag",
    "label": "Unix",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-31"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB17-24",
    "taxonomy": "iab-qag",
    "label": "Paintball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-24"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB11-1",
    "taxonomy": "iab-qag",
    "label": "Immigration",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11"
    }]
    }, {
    "id": "IAB19-20",
    "taxonomy": "iab-qag",
    "label": "JavaScript",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-20"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB20-11",
    "taxonomy": "iab-qag",
    "label": "Caribbean",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB2-17",
    "taxonomy": "iab-qag",
    "label": "Performance Vehicles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-17"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB17-25",
    "taxonomy": "iab-qag",
    "label": "Power & Motorcycles",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-25"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB11",
    "taxonomy": "iab-qag",
    "label": "Law, Gov’t & Politics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB11"
    }]
    }, {
    "id": "IAB19-15",
    "taxonomy": "iab-qag",
    "label": "Email",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-15"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB19-6",
    "taxonomy": "iab-qag",
    "label": "Cell Phones",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB8-5",
    "taxonomy": "iab-qag",
    "label": "Cocktails/Beer",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB9-28",
    "taxonomy": "iab-qag",
    "label": "Screenwriting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-28"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB12-3",
    "taxonomy": "iab-qag",
    "label": "Local News",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB12-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB12"
    }]
    }, {
    "id": "IAB13-5",
    "taxonomy": "iab-qag",
    "label": "Hedge Fund",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB2-6",
    "taxonomy": "iab-qag",
    "label": "Convertible",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB2-21",
    "taxonomy": "iab-qag",
    "label": "Trucks & Accessories",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-21"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB20-22",
    "taxonomy": "iab-qag",
    "label": "National Parks",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-22"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB13-11",
    "taxonomy": "iab-qag",
    "label": "Stocks",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB3-12",
    "taxonomy": "iab-qag",
    "label": "Metals",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-12"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB17-20",
    "taxonomy": "iab-qag",
    "label": "Martial Arts",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-20"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB17-13",
    "taxonomy": "iab-qag",
    "label": "Freshwater Fishing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-13"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB7-27",
    "taxonomy": "iab-qag",
    "label": "IBS/Crohn's Disease",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-27"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB17-19",
    "taxonomy": "iab-qag",
    "label": "Inline Skating",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-19"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB16-5",
    "taxonomy": "iab-qag",
    "label": "Large Animals",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16"
    }]
    }, {
    "id": "IAB26",
    "taxonomy": "iab-qag",
    "label": "Illegal Content",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB26"
    }]
    }, {
    "id": "IAB19-1",
    "taxonomy": "iab-qag",
    "label": "3-D Graphics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB2-11",
    "taxonomy": "iab-qag",
    "label": "Hatchback",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB6-7",
    "taxonomy": "iab-qag",
    "label": "Pregnancy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6"
    }]
    }, {
    "id": "IAB23-6",
    "taxonomy": "iab-qag",
    "label": "Hinduism",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB10-5",
    "taxonomy": "iab-qag",
    "label": "Home Repair",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10"
    }]
    }, {
    "id": "IAB19-35",
    "taxonomy": "iab-qag",
    "label": "Web Search",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-35"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB7-16",
    "taxonomy": "iab-qag",
    "label": "Deafness",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-16"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB8-12",
    "taxonomy": "iab-qag",
    "label": "Health/Lowfat Cooking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-12"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB1-2",
    "taxonomy": "iab-qag",
    "label": "Celebrity Fan/Gossip",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1"
    }]
    }, {
    "id": "IAB9-27",
    "taxonomy": "iab-qag",
    "label": "Scrapbooking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-27"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB14-2",
    "taxonomy": "iab-qag",
    "label": "Divorce Support",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14"
    }]
    }, {
    "id": "IAB10-4",
    "taxonomy": "iab-qag",
    "label": "Gardening",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10"
    }]
    }, {
    "id": "IAB12-2",
    "taxonomy": "iab-qag",
    "label": "National News",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB12-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB12"
    }]
    }, {
    "id": "IAB13-9",
    "taxonomy": "iab-qag",
    "label": "Options",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB17-26",
    "taxonomy": "iab-qag",
    "label": "Pro Basketball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-26"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB9-16",
    "taxonomy": "iab-qag",
    "label": "Guitar",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-16"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB23-5",
    "taxonomy": "iab-qag",
    "label": "Christianity",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB23"
    }]
    }, {
    "id": "IAB7-4",
    "taxonomy": "iab-qag",
    "label": "Allergies",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB2-14",
    "taxonomy": "iab-qag",
    "label": "MiniVan",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-14"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB18-3",
    "taxonomy": "iab-qag",
    "label": "Fashion",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18"
    }]
    }, {
    "id": "IAB17-15",
    "taxonomy": "iab-qag",
    "label": "Golf",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-15"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB17-39",
    "taxonomy": "iab-qag",
    "label": "Table Tennis/Ping-Pong",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-39"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB3-8",
    "taxonomy": "iab-qag",
    "label": "Green Solutions",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB9-31",
    "taxonomy": "iab-qag",
    "label": "Woodworking",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-31"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB20-18",
    "taxonomy": "iab-qag",
    "label": "Hotels",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-18"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB19-18",
    "taxonomy": "iab-qag",
    "label": "Internet Technology",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-18"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB14-6",
    "taxonomy": "iab-qag",
    "label": "Teens",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14"
    }]
    }, {
    "id": "IAB17-2",
    "taxonomy": "iab-qag",
    "label": "Baseball",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB19-29",
    "taxonomy": "iab-qag",
    "label": "Entertainment",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-29"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB9-3",
    "taxonomy": "iab-qag",
    "label": "Beadwork",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB17-32",
    "taxonomy": "iab-qag",
    "label": "Saltwater Fishing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-32"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB26-1",
    "taxonomy": "iab-qag",
    "label": "Illegal Content",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB26-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB26"
    }]
    }, {
    "id": "IAB7-8",
    "taxonomy": "iab-qag",
    "label": "Autism/PDD",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB5-11",
    "taxonomy": "iab-qag",
    "label": "Homework/Study Tips",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB8-13",
    "taxonomy": "iab-qag",
    "label": "Italian Cuisine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-13"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB2",
    "taxonomy": "iab-qag",
    "label": "Automotive",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB7-13",
    "taxonomy": "iab-qag",
    "label": "Chronic Fatigue Syndrome",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-13"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB4-9",
    "taxonomy": "iab-qag",
    "label": "Telecommuting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB2-3",
    "taxonomy": "iab-qag",
    "label": "Buying/Selling Cars",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB25-3",
    "taxonomy": "iab-qag",
    "label": "Pornography",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25"
    }]
    }, {
    "id": "IAB7-42",
    "taxonomy": "iab-qag",
    "label": "Substance Abuse",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-42"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB7-11",
    "taxonomy": "iab-qag",
    "label": "Cancer",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB7-31",
    "taxonomy": "iab-qag",
    "label": "Men's Health",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-31"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB14",
    "taxonomy": "iab-qag",
    "label": "Society",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14"
    }]
    }, {
    "id": "IAB13-4",
    "taxonomy": "iab-qag",
    "label": "Financial Planning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB19-34",
    "taxonomy": "iab-qag",
    "label": "Web Design/HTML",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-34"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB20-8",
    "taxonomy": "iab-qag",
    "label": "By US Locale",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB4-8",
    "taxonomy": "iab-qag",
    "label": "Scholarships",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB20-25",
    "taxonomy": "iab-qag",
    "label": "Theme Parks",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-25"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB9-19",
    "taxonomy": "iab-qag",
    "label": "Jewelry Making",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-19"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB16-4",
    "taxonomy": "iab-qag",
    "label": "Dogs",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16"
    }]
    }, {
    "id": "IAB26-4",
    "taxonomy": "iab-qag",
    "label": "Copyright Infringement",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB26-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB26"
    }]
    }, {
    "id": "IAB5-6",
    "taxonomy": "iab-qag",
    "label": "Distance Learning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB21",
    "taxonomy": "iab-qag",
    "label": "Real Estate",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB21"
    }]
    }, {
    "id": "IAB2-18",
    "taxonomy": "iab-qag",
    "label": "Pickup",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-18"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB5-10",
    "taxonomy": "iab-qag",
    "label": "Homeschooling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB19-23",
    "taxonomy": "iab-qag",
    "label": "Net Conferencing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-23"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB19-2",
    "taxonomy": "iab-qag",
    "label": "Animation",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB19-5",
    "taxonomy": "iab-qag",
    "label": "Cameras & Camcorders",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB8-17",
    "taxonomy": "iab-qag",
    "label": "Vegetarian",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-17"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB21-2",
    "taxonomy": "iab-qag",
    "label": "Architects",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB21-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB21"
    }]
    }, {
    "id": "IAB15-10",
    "taxonomy": "iab-qag",
    "label": "Weather",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }, {
    "id": "IAB5-8",
    "taxonomy": "iab-qag",
    "label": "Language Learning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB7-24",
    "taxonomy": "iab-qag",
    "label": "Heart Disease",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-24"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB17-33",
    "taxonomy": "iab-qag",
    "label": "Scuba Diving",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-33"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB17-23",
    "taxonomy": "iab-qag",
    "label": "Olympics",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-23"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB7-17",
    "taxonomy": "iab-qag",
    "label": "Dental Care",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-17"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB17-12",
    "taxonomy": "iab-qag",
    "label": "Football",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-12"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB18-1",
    "taxonomy": "iab-qag",
    "label": "Beauty",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18"
    }]
    }, {
    "id": "IAB7-22",
    "taxonomy": "iab-qag",
    "label": "GERD/Acid Reflux",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-22"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB19-14",
    "taxonomy": "iab-qag",
    "label": "Desktop Video",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-14"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB10",
    "taxonomy": "iab-qag",
    "label": "Home & Garden",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10"
    }]
    }, {
    "id": "IAB13-8",
    "taxonomy": "iab-qag",
    "label": "Mutual Funds",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB13"
    }]
    }, {
    "id": "IAB16-3",
    "taxonomy": "iab-qag",
    "label": "Cats",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB16"
    }]
    }, {
    "id": "IAB5-14",
    "taxonomy": "iab-qag",
    "label": "Special Education",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-14"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB9-2",
    "taxonomy": "iab-qag",
    "label": "Arts & Crafts",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB4-11",
    "taxonomy": "iab-qag",
    "label": "Career Advice",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB8-11",
    "taxonomy": "iab-qag",
    "label": "French Cuisine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB20-5",
    "taxonomy": "iab-qag",
    "label": "Bed & Breakfasts",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB19-27",
    "taxonomy": "iab-qag",
    "label": "PC Support",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-27"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB25",
    "taxonomy": "iab-qag",
    "label": "Non-Standard Content",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB25"
    }]
    }, {
    "id": "IAB22-2",
    "taxonomy": "iab-qag",
    "label": "Couponing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB22-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB22"
    }]
    }, {
    "id": "IAB7-36",
    "taxonomy": "iab-qag",
    "label": "Physical Therapy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-36"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB8-6",
    "taxonomy": "iab-qag",
    "label": "Coffee/Tea",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB3-4",
    "taxonomy": "iab-qag",
    "label": "Business Software",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB7",
    "taxonomy": "iab-qag",
    "label": "Health & Fitness",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB2-9",
    "taxonomy": "iab-qag",
    "label": "Diesel",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB10-6",
    "taxonomy": "iab-qag",
    "label": "Home Theater",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10"
    }]
    }, {
    "id": "IAB1-3",
    "taxonomy": "iab-qag",
    "label": "Fine Art",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1"
    }]
    }, {
    "id": "IAB7-5",
    "taxonomy": "iab-qag",
    "label": "Alternative Medicine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB7-28",
    "taxonomy": "iab-qag",
    "label": "Incest/Abuse Support",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-28"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB4-1",
    "taxonomy": "iab-qag",
    "label": "Career Planning",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB19-10",
    "taxonomy": "iab-qag",
    "label": "Computer Reviews",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB10-7",
    "taxonomy": "iab-qag",
    "label": "Interior Decorating",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10"
    }]
    }, {
    "id": "IAB6-4",
    "taxonomy": "iab-qag",
    "label": "Family Internet",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6"
    }]
    }, {
    "id": "IAB9-6",
    "taxonomy": "iab-qag",
    "label": "Candle & Soap Making",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB20-15",
    "taxonomy": "iab-qag",
    "label": "France",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-15"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB17-27",
    "taxonomy": "iab-qag",
    "label": "Pro Ice Hockey",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-27"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB9-7",
    "taxonomy": "iab-qag",
    "label": "Card Games",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB3-5",
    "taxonomy": "iab-qag",
    "label": "Construction",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB20-1",
    "taxonomy": "iab-qag",
    "label": "Adventure Travel",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB19-19",
    "taxonomy": "iab-qag",
    "label": "Java",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19-19"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB19"
    }]
    }, {
    "id": "IAB18-4",
    "taxonomy": "iab-qag",
    "label": "Jewelry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18"
    }]
    }, {
    "id": "IAB6-1",
    "taxonomy": "iab-qag",
    "label": "Adoption",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB6"
    }]
    }, {
    "id": "IAB8-9",
    "taxonomy": "iab-qag",
    "label": "Dining Out",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-9"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB3-11",
    "taxonomy": "iab-qag",
    "label": "Marketing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-11"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB20-26",
    "taxonomy": "iab-qag",
    "label": "Traveling with Kids",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-26"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB9-21",
    "taxonomy": "iab-qag",
    "label": "Needlework",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-21"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB2-10",
    "taxonomy": "iab-qag",
    "label": "Electric Vehicle",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB2"
    }]
    }, {
    "id": "IAB17-40",
    "taxonomy": "iab-qag",
    "label": "Tennis",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-40"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB8-2",
    "taxonomy": "iab-qag",
    "label": "Barbecues & Grilling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB4-6",
    "taxonomy": "iab-qag",
    "label": "Resume Writing/Advice",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-6"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB15-3",
    "taxonomy": "iab-qag",
    "label": "Chemistry",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }, {
    "id": "IAB14-1",
    "taxonomy": "iab-qag",
    "label": "Dating",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14"
    }]
    }, {
    "id": "IAB1-4",
    "taxonomy": "iab-qag",
    "label": "Humor",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1-4"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB1"
    }]
    }, {
    "id": "IAB9-10",
    "taxonomy": "iab-qag",
    "label": "Collecting",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-10"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB7-1",
    "taxonomy": "iab-qag",
    "label": "Exercise",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB17-7",
    "taxonomy": "iab-qag",
    "label": "Cheerleading",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB12-1",
    "taxonomy": "iab-qag",
    "label": "International News",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB12-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB12"
    }]
    }, {
    "id": "IAB22-3",
    "taxonomy": "iab-qag",
    "label": "Comparison",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB22-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB22"
    }]
    }, {
    "id": "IAB20-19",
    "taxonomy": "iab-qag",
    "label": "Italy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-19"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB18",
    "taxonomy": "iab-qag",
    "label": "Style & Fashion",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB18"
    }]
    }, {
    "id": "IAB9-15",
    "taxonomy": "iab-qag",
    "label": "Getting Published",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9-15"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB9"
    }]
    }, {
    "id": "IAB3-1",
    "taxonomy": "iab-qag",
    "label": "Advertising",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-1"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB7-32",
    "taxonomy": "iab-qag",
    "label": "Nutrition",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7-32"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB7"
    }]
    }, {
    "id": "IAB17-16",
    "taxonomy": "iab-qag",
    "label": "Horse Racing",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-16"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB8-14",
    "taxonomy": "iab-qag",
    "label": "Japanese Cuisine",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8-14"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB8"
    }]
    }, {
    "id": "IAB5-15",
    "taxonomy": "iab-qag",
    "label": "Studying Business",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5-15"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB5"
    }]
    }, {
    "id": "IAB10-3",
    "taxonomy": "iab-qag",
    "label": "Environmental Safety",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB10"
    }]
    }, {
    "id": "IAB17-38",
    "taxonomy": "iab-qag",
    "label": "Swimming",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-38"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB4-2",
    "taxonomy": "iab-qag",
    "label": "College",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4-2"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB4"
    }]
    }, {
    "id": "IAB15-7",
    "taxonomy": "iab-qag",
    "label": "Space/Astronomy",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }, {
    "id": "IAB17-44",
    "taxonomy": "iab-qag",
    "label": "World Soccer",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-44"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB20-14",
    "taxonomy": "iab-qag",
    "label": "Europe",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20-14"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB20"
    }]
    }, {
    "id": "IAB14-5",
    "taxonomy": "iab-qag",
    "label": "Senior Living",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14-5"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB14"
    }]
    }, {
    "id": "IAB3-7",
    "taxonomy": "iab-qag",
    "label": "Government",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3-7"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB3"
    }]
    }, {
    "id": "IAB17-3",
    "taxonomy": "iab-qag",
    "label": "Bicycling",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17-3"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB17"
    }]
    }, {
    "id": "IAB15-8",
    "taxonomy": "iab-qag",
    "label": "Geography",
    "links": [{
        "rel": "self",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15-8"
    }, {
        "rel": "parent",
        "link": "https://api.aylien.com/api/v1/classify/taxonomy/iab-qag/IAB15"
    }]
    }]
