import React from "react";
import { DocsThemeConfig } from "nextra-theme-docs";
import { useRouter } from "next/router";

const config: DocsThemeConfig = {
  logo: <span>Sao Khuê</span>,
  project: {
    link: "https://github.com/lovesaokhue/lovesaokhue.github.io",
  },
  docsRepositoryBase:
    "https://github.com/lovesaokhue/lovesaokhue.github.io/tree/main",
  footer: {
    text: "Sao Khuê",
  },
  useNextSeoProps() {
    const router = useRouter();
    const canonicalUrl = (
      `https://lovesaokhue.github.io` + (router.asPath === "/" ? "" : router.asPath)
    ).split("?")[0];

    return {
      titleTemplate: "%s",
      canonical: canonicalUrl,
      twitter: {
        cardType: "summary_large_image",
        site: "@lovesaokhue",
        handle: "@lovesaokhue",
      },
    };
  },
  head: (
    <>
      <meta name="msapplication-TileColor" content="#fff" />
      <meta httpEquiv="Content-Language" content="vi" />
      <meta
        name="description"
        content="Sao Khuê: Wanderer"
      />
      <meta property="og:title" content="Sao Khuê" />
      <meta property="og:description" content="Wanderer" />
      <meta name="apple-mobile-web-app-title" content="Mốc Meo" />
    </>
  ),
};

export default config;
