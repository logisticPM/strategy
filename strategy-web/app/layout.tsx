import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Lululemon · 战略工作台",
  description: "保护品牌，重启盈利增长。企业战略、证据与决策。",
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <body className="antialiased">{children}</body>
    </html>
  );
}
