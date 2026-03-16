import { simulateNetwork } from "./transport";

export type LoginRequest = { username: string; password: string };

export async function login(body: LoginRequest): Promise<string> {
  // pretend to call backend auth controller
  const response = await simulateNetwork({
    path: "/auth/login",
    body,
  });
  return response.token as string;
}
