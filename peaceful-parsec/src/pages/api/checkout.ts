export const prerender = false;

import type { APIRoute } from "astro";
import { Polar } from "@polar-sh/sdk";
import { getPostHogServer } from "../../lib/posthog-server";

export const GET: APIRoute = async ({ request, redirect }) => {
  const url = new URL(request.url);
  const productId = url.searchParams.get("products");

  if (!productId) {
    return new Response("Missing products parameter", { status: 400 });
  }

  const posthog = getPostHogServer();
  posthog.capture({
    distinctId: request.headers.get("x-forwarded-for") || "anonymous",
    event: "checkout_session_created",
    properties: {
      product: "698 skills para Claude Code",
      price: 12,
      currency: "USD",
    },
  });

  const polar = new Polar({
    accessToken: import.meta.env.POLAR_ACCESS_TOKEN,
    server: "production",
  });

  const checkout = await polar.checkouts.create({
    products: [productId],
    successUrl: import.meta.env.POLAR_SUCCESS_URL,
    theme: "light",
  });

  return redirect(checkout.url);
};
