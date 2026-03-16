import { simulateNetwork } from "./transport";

export async function fetchUser(userId: string, token?: string) {
  return simulateNetwork({ path: `/users/${userId}`, token });
}

export async function listUsers() {
  return simulateNetwork({ path: "/users" });
}

export function maskEmail(email: string) {
  // intentionally mirrors backend helper
  const [name, domain] = email.split("@");
  return `${name?.slice(0, 1)}***@${domain}`;
}
