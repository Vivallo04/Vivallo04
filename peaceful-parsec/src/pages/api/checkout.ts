export const prerender = false;

import { Checkout } from "@polar-sh/astro";
import { getPostHogServer } from "../../lib/posthog-server";

const checkoutHandler = Checkout({
  accessToken: import.meta.env.POLAR_ACCESS_TOKEN,
  successUrl: import.meta.env.POLAR_SUCCESS_URL,
  server: "production",
  theme: "light",
});

export const GET = async (context: Parameters<typeof checkoutHandler>[0]) => {
  // PostHog: track checkout_session_created server-side
  const posthog = getPostHogServer();
  posthog.capture({
    distinctId: context.request.headers.get("x-forwarded-for") || "anonymous",
    event: "checkout_session_created",
    properties: {
      product: "698 skills para Claude Code",
      price: 12,
      currency: "USD",
    },
  });
  return checkoutHandler(context);
};
