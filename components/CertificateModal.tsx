"use client";

import React, { useEffect } from "react";

interface CertificateModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  issuer: string;
  imageUrl: string;
  pdfUrl: string;
  lang: "pl" | "en";
}

export default function CertificateModal({
  isOpen,
  onClose,
  title,
  issuer,
  imageUrl,
  pdfUrl,
  lang,
}: CertificateModalProps) {
  // Prevent background scroll when modal is open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "unset";
    }
    return () => {
      document.body.style.overflow = "unset";
    };
  }, [isOpen]);

  // Handle escape key to close
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [onClose]);

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6"
      style={{
        background: "rgba(10, 9, 8, 0.85)",
        backdropFilter: "blur(8px)",
        WebkitBackdropFilter: "blur(8px)",
      }}
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-4xl rounded-xl overflow-hidden shadow-2xl flex flex-col transition-all duration-300 transform scale-100 opacity-100"
        style={{
          background: "var(--bg-2)",
          border: "1px solid var(--border-2)",
          maxHeight: "90vh",
        }}
        onClick={(e: React.MouseEvent) => e.stopPropagation()}
      >
        {/* Header */}
        <div
          className="flex items-center justify-between px-6 py-4"
          style={{ borderBottom: "1px solid var(--border)" }}
        >
          <div>
            <h3
              className="font-bold text-base sm:text-lg"
              style={{ color: "var(--fg)", lineHeight: 1.2 }}
            >
              {title}
            </h3>
            <p
              className="text-xs mt-1"
              style={{
                fontFamily: "var(--font-jetbrains), Consolas, monospace",
                color: "var(--accent)",
              }}
            >
              {issuer}
            </p>
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full flex items-center justify-center text-xl transition-colors duration-150 hover:bg-white/10 hover:text-white"
            style={{ color: "var(--fg-2)" }}
            aria-label="Close"
          >
            &times;
          </button>
        </div>

        {/* Image Container */}
        <div
          className="flex-1 overflow-y-auto p-4 md:p-6 flex items-center justify-center"
          style={{ background: "rgba(0, 0, 0, 0.2)" }}
        >
          <img
            src={imageUrl}
            alt={title}
            className="max-w-full max-h-[60vh] object-contain rounded shadow-lg border border-white/5"
          />
        </div>

        {/* Footer Actions */}
        <div
          className="px-6 py-4 flex flex-wrap items-center justify-between gap-3"
          style={{ borderTop: "1px solid var(--border)" }}
        >
          <div className="flex gap-3">
            <a
              href={pdfUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="px-4 py-2 rounded font-medium transition-all duration-150 text-xs flex items-center gap-1.5 hover:brightness-110 active:scale-95"
              style={{
                background: "var(--accent)",
                color: "#1a1916",
              }}
            >
              <span>{lang === "pl" ? "Otwórz PDF" : "Open PDF"}</span>
              <span>&rarr;</span>
            </a>
            <a
              href={pdfUrl}
              download="Certificate_Kacper_Kleczaj_Bielik.pdf"
              className="px-4 py-2 rounded font-medium transition-all duration-150 text-xs flex items-center gap-1.5 hover:text-white hover:border-white/20 active:scale-95"
              style={{
                background: "var(--bg-3)",
                color: "var(--fg-2)",
                border: "1px solid var(--border)",
              }}
            >
              <span>{lang === "pl" ? "Pobierz" : "Download"}</span>
            </a>
          </div>
          <button
            onClick={onClose}
            className="px-4 py-2 rounded font-medium transition-colors duration-150 text-xs hover:text-[var(--fg-2)]"
            style={{
              background: "transparent",
              color: "var(--fg-3)",
            }}
          >
            {lang === "pl" ? "Zamknij" : "Close"}
          </button>
        </div>
      </div>
    </div>
  );
}
