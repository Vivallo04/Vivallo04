export const prerender = false;

import { Checkout } from "@polar-sh/astro";

export const GET = Checkout({
  accessToken: import.meta.env.POLAR_ACCESS_TOKEN,
  successUrl: import.meta.env.POLAR_SUCCESS_URL,
  server: "production",
  theme: "light",
});
