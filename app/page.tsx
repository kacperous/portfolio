import Navigation from "@/components/Navigation";
import Hero from "@/components/Hero";
import Experience from "@/components/Experience";
import Projects from "@/components/Projects";
import Hackathons from "@/components/Hackathons";
import Technologies from "@/components/Technologies";
import Education from "@/components/Education";
import Contact from "@/components/Contact";
import { LangProvider } from "@/components/LanguageSwitcher";

export default function Home() {
  return (
    <LangProvider>
      <main className="relative">
        <Navigation />
        <Hero />

        <Experience />
        <Projects />
        <Hackathons />
        <Technologies />
        <Education />

        <Contact />
      </main>
    </LangProvider>
  );
}
