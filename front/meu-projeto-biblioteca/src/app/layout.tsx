import React, { ReactNode } from 'react';
import Link from 'next/link';
import './globals.css';

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <html lang="pt-BR">
      <head>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Biblioteca F11</title>
      </head>
      <body>
        <header>
          <h1>bibliotecaF11</h1>
          <nav>
            <Link href="/">Home</Link>
          </nav>
        </header>
        <main>
          {children}
        </main>
      </body>
    </html>
  );
};

export default Layout;
