export type Lang = "pl" | "en";

export const i18n = {
  pl: {
    hero: {
      badge: "OTWARTY NA PROJEKTY",
      typewriter: ["Full Stack Developer", "Web & Mobile Developer", "React & Python Engineer"],
      attrs: [
        { key: "lokalizacja", val: "Łódź, PL" },
        { key: "uczelnia", val: "Politechnika Łódzka" },
        { key: "stopień", val: "inżynier (w trakcie)" },
      ],
      bio: "Projektuję i buduję strony internetowe, aplikacje webowe i mobilne — od pomysłu po wdrożenie. Pomogę Ci stworzyć produkt, który działa i sprzedaje.",
      cta: "Zobacz projekty",
      stats: [
        { value: "4", label: "hackathony '25" },
        { value: "2×", label: "1. miejsce" },
        { value: "1.5", label: "roku doświadczenia" },
      ],
    },
    experience: {
      label: "Doświadczenie",
      title: "Praca zawodowa",
      now: "TERAZ",
      items: [
        {
          description: "Pełna odpowiedzialność za architekturę i rozwój GreenTransit — systemu eCMR do elektronicznego obiegu dokumentów transportowych. Platforma PWA na AWS, eliminuje papier w branży TSL.",
          points: [
            "Całościowa odpowiedzialność za architekturę i kod aplikacji",
            "Backend: FastAPI + Alembic (migracje) + PyTest (testy)",
            "Frontend: React + TypeScript",
            "Infrastruktura: AWS, offline PWA, integracje z TMS/WMS/ERP",
          ],
        },
        {
          description: "Projektowanie systemów do automatycznego zbierania i przetwarzania danych z różnych źródeł internetowych.",
          points: [
            "Narzędzia web scrapingowe do pozyskiwania dokumentów publicznych",
            "Walidacja i standaryzacja danych",
            "Optymalizacja przetwarzania dużych wolumenów",
          ],
        },
        {
          description: "Tworzenie aplikacji webowych i sklepów internetowych. Pełna odpowiedzialność za wdrożenie od analizy po utrzymanie.",
          points: [
            "Aplikacje webowe: Django + React/TypeScript",
            "Sklepy: WordPress/WooCommerce",
            "End-to-end: od analizy do produkcji",
          ],
        },
        {
          description: "Aplikacje webowe w Spring Boot + React. Agile/Scrum.",
          points: [
            "Projektowanie backendu i frontendu",
            "Optymalizacja kodu i baz danych",
            "Praca zespołowa w Agile/Scrum",
          ],
        },
      ],
    },
    projects: {
      label: "Portfolio",
      title: "Projekty",
      descriptions: [
        'Aplikacja do zmiany nawyków żywieniowych — zasada "12 miesięcy, 12 nawyków". AI licznik kalorii z analizą zdjęć. Grywalizacja i moduł rodzic-dziecko.',
        "Mobilna aplikacja do zarządzania wspólnymi wydatkami. Automatyczne rozliczanie długów, raporty wydatków i synchronizacja w czasie rzeczywistym.",
        "Platforma do współdzielenia list zakupów via WebSockety. Google Login, SMS weryfikacja, Stripe subskrypcje.",
        "AI system do wykrywania pojazdów bez filtra DPF z kamer miejskich. Integracja z CEPiK do automatycznego raportowania naruszeń.",
        "Aplikacja agregująca dane o lekach, alerty prawne i dane rynkowe — dedykowana farmaceutom i menedżerom aptecznym.",
        "Rozszerzenie karty Łodzianina o grywalizację dzielnic. Nagradza mieszkańców za aktywność w lokalnej społeczności i wsparcie lokalnych firm.",
      ],
    },
    hackathons: {
      label: "Osiągnięcia",
      title: "Hackathony",
      stats: ["hackathony w 2025", "pierwsze miejsce", "drugie miejsce"],
      team: "zespół:",
      items: [
        "Grywalizacja karty Łodzianina — angażuje mieszkańców we wsparcie lokalnych firm i inicjatywy miejskie.",
        "Mobilna aplikacja do zdrowych nawyków żywieniowych dzieci z AI, quizami, modułem Roblox i grywalizacją.",
        "AI system do wykrywania pojazdów z usuniętym DPF z kamer miejskich + integracja z CEPiK.",
        "Agregator danych o lekach, alertów prawnych i danych rynkowych dla farmaceutów.",
      ],
    },
    tech: {
      label: "Stack",
      title: "Technologie",
      dbLabel: "Bazy danych",
    },
    education: {
      label: "Edukacja",
      title: "Wykształcenie & Certyfikaty",
      items: [
        { degree: "Informatyka Stosowana", type: "Studia inżynierskie", period: "2023 — obecnie" },
        { degree: "Technik Informatyk", type: "Szkoła techniczna", period: "2019 — 2023" },
      ],
      certsLabel: "Certyfikaty",
    },
    contact: {
      label: "Kontakt",
      title: "Porozmawiajmy",
      body: "Potrzebujesz strony internetowej, aplikacji webowej lub mobilnej? Jestem otwarty na nowe projekty i zlecenia. Napisz — odpowiem szybko.",
      cta: "Napisz do mnie →",
    },
  },

  en: {
    hero: {
      badge: "OPEN FOR PROJECTS",
      typewriter: ["Full Stack Developer", "Web & Mobile Developer", "React & Python Engineer"],
      attrs: [
        { key: "location", val: "Łódź, Poland" },
        { key: "university", val: "Lodz University of Technology" },
        { key: "degree", val: "engineer (in progress)" },
      ],
      bio: "I design and build websites, web apps and mobile apps — from idea to deployment. I'll help you create a product that works and converts.",
      cta: "See projects",
      stats: [
        { value: "4", label: "hackathons '25" },
        { value: "2×", label: "1st place" },
        { value: "1.5", label: "year of experience" },
      ],
    },
    experience: {
      label: "Experience",
      title: "Work",
      now: "NOW",
      items: [
        {
          description: "Full ownership of GreenTransit architecture — an eCMR system for digital transport document flow. AWS-hosted PWA eliminating paperwork in the TSL industry.",
          points: [
            "End-to-end ownership of application architecture and code",
            "Backend: FastAPI + Alembic (migrations) + PyTest (testing)",
            "Frontend: React + TypeScript",
            "Infrastructure: AWS, offline PWA, TMS/WMS/ERP integrations",
          ],
        },
        {
          description: "Designing systems for automated collection and processing of data from various online sources.",
          points: [
            "Web scraping tools for public document retrieval",
            "Data validation and standardization",
            "Optimization for large-volume data processing",
          ],
        },
        {
          description: "Building web applications and e-commerce stores. Full ownership from analysis to maintenance.",
          points: [
            "Web apps: Django + React/TypeScript",
            "Stores: WordPress/WooCommerce",
            "End-to-end: from analysis to production",
          ],
        },
        {
          description: "Web applications with Spring Boot + React. Agile/Scrum workflow.",
          points: [
            "Backend and frontend design",
            "Code and database optimization",
            "Team collaboration in Agile/Scrum",
          ],
        },
      ],
    },
    projects: {
      label: "Portfolio",
      title: "Projects",
      descriptions: [
        'Habit-changing nutrition app — "12 months, 12 habits" principle. AI calorie counter with photo analysis. Gamification and parent-child module.',
        "Mobile app for managing shared expenses. Automatic debt settlement, spending reports and real-time synchronization.",
        "Shared shopping list platform via WebSockets. Google Login, SMS verification, Stripe subscriptions.",
        "AI system for detecting vehicles without DPF filters from city cameras. Integration with CEPiK for automatic violation reporting.",
        "App aggregating drug data, legal alerts and market data — dedicated to pharmacists and pharmacy managers.",
        "Extension of the Łodzianin city card with district gamification. Rewards residents for local community activity and supporting local businesses.",
      ],
    },
    hackathons: {
      label: "Achievements",
      title: "Hackathons",
      stats: ["hackathons in 2025", "first place", "second place"],
      team: "team:",
      items: [
        "Gamification of the Łodzianin city card — engages residents in supporting local businesses and city initiatives.",
        "Mobile app for children's healthy eating habits with AI, quizzes, Roblox module and gamification.",
        "AI system for detecting vehicles with removed DPF filters from city cameras + CEPiK integration.",
        "Aggregator of drug data, legal alerts and market data for pharmacists.",
      ],
    },
    tech: {
      label: "Stack",
      title: "Technologies",
      dbLabel: "Databases",
    },
    education: {
      label: "Education",
      title: "Education & Certifications",
      items: [
        { degree: "Applied Computer Science", type: "Engineering degree", period: "2023 — present" },
        { degree: "IT Technician", type: "Technical high school", period: "2019 — 2023" },
      ],
      certsLabel: "Certifications",
    },
    contact: {
      label: "Contact",
      title: "Let's talk",
      body: "Need a website, web app or mobile app? I'm open to new projects and freelance work. Write to me — I respond quickly.",
      cta: "Write to me →",
    },
  },
} as const;
