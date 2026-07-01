events = [
    ("Japan Expo", "2026-07-09", "Paris Nord Villepinte"),
    ("Village International de la Gastronomie", "2026-09-10", "Quai Branly"),
    ("Mondial de l'automobile", "2026-10-12", "Paris Expo Porte de Versailles"),
    ("Paris Games Week", "2026-10-22", "Paris Expo Porte de Versailles"),
    ("Art Basel Paris", "2026-10-23", "Grand Palais"),
    ("Salon du Chocolat", "2026-10-28", "Paris Expo Porte de Versailles"),
    ("Paris Photo", "2026-11-11", "Grand Palais"),
    ("MIF Expo", "2026-11-12", "Paris Expo Porte de Versailles"),
    ("Créations & Savoir-Faire", "2026-11-18", "Paris Expo Porte de Versailles"),
    ("Le Grand Tasting", "2026-11-28", "Carrousel du Louvre"),
]

ics = [
"BEGIN:VCALENDAR",
"VERSION:2.0",
"PRODID:-//Salons Paris//FR"
]

for name, date, place in events:
    ics += [
        "BEGIN:VEVENT",
        f"DTSTART;VALUE=DATE:{date.replace('-', '')}",
        f"SUMMARY:{name}",
        f"LOCATION:{place}",
        "END:VEVENT"
    ]

ics.append("END:VCALENDAR")

open("salons-paris.ics","w",encoding="utf-8").write("\n".join(ics))
