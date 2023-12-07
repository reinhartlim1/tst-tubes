"use client";
import { ChakraProvider } from "@chakra-ui/react";
import WithSubnavigation from "@/components/Navbar";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <ChakraProvider>
          <div>
            <WithSubnavigation />
            {children}
          </div>
        </ChakraProvider>
      </body>
    </html>
  );
}
