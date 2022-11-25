import scrapy
from ..items import BestItem


class Spyder(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://consulentidellavoro.mi.it/ordine/gli-iscritti-allordine/',
    ]

    def parse(self, response, **kwargs):
        items = BestItem()

        Numeros = response.css('small:nth-child(3)::text').extract()
        PEC = response.css('tr~ tr+ tr td+ td::text').extract()
        Codicefiscale = response.css('small~ small::text').extract()
        Codice_fiscale = ([Codice_fiscale.replace('Codice fiscale:', '') for Codice_fiscale in Codicefiscale])

        Status = response.css('.studioDetails small::text').extract()
        Nome = response.xpath('//*[@id="post-70"]/div/div[2]/div[1]/div/div/text()').extract()
        s = ([s.replace('\n', '') for s in Nome])
        p = ([p.replace('  ', '') for p in s])
        p = list(filter(('').__ne__, p))

        Indirizzo_citta_provincia = response.css('tr:nth-child(2) td+ td::text').extract()
        a = ([a.replace('\n', '') for a in Indirizzo_citta_provincia])
        b = ([b.replace('  ', '') for b in a])

        indirizzo = 0
        citta_provincia = 1
        nome = 0

        for numero, codice_fiscale, pec, status, i, h in zip(Numeros, Codice_fiscale, PEC, Status, p, b):
            cp = str(b[citta_provincia])
            citta = cp.split('-')[0]
            provincia = cp.split('-')[1]

            items['bNumero'] = numero
            items['cCodice_fiscale'] = codice_fiscale
            items['dPEC'] = pec
            items['eStatus'] = status
            items['aNome'] = p[nome]
            items['fIndirizzo'] = b[indirizzo]
            items['gCitta'] = citta
            items['hProvincia'] = provincia

            nome = nome + 1
            indirizzo = indirizzo + 2
            citta_provincia = citta_provincia + 2
            yield items

        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
