import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-jetbrains",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Kacper Kleczaj — Full Stack Developer",
  description:
    "Portfolio of Kacper Kleczaj — Full Stack Developer specializing in React, Python/Django, and modern web technologies. Based in Łódź, Poland.",
  keywords: [
    "Full Stack Developer",
    "React",
    "Python",
    "Django",
    "TypeScript",
    "Portfolio",
    "Łódź",
  ],
  authors: [{ name: "Kacper Kleczaj" }],
  icons: {
    icon: "/icon.png",
    apple: "/icon.png",
  },
  openGraph: {
    title: "Kacper Kleczaj — Full Stack Developer",
    description:
      "Full Stack Developer specializing in React, Python, Django, and modern web technologies.",
    type: "website",
    locale: "pl_PL",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pl" className={`${inter.variable} ${jetbrainsMono.variable}`}>
      <body className="antialiased">{children}</body>
    </html>
  );
}
