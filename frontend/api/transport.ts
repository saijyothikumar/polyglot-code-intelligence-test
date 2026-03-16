type Request = { path: string; body?: any; token?: string };

// Very naive simulated transport layer used by both authApi and userApi
export async function simulateNetwork(req: Request): Promise<any> {
  // note: this mirrors backend/demo_flow logic but leaves gaps
  if (req.path.startsWith("/auth")) {
    return { token: `token-${req.body?.username}` };
  }
  if (req.path.startsWith("/users/")) {
    const id = req.path.replace("/users/", "");
    return { id, email: `${id}@example.com`, masked_email: `${id[0]}***@example.com` };
  }
  if (req.path === "/users") {
    return [
      { id: "alice", email: "alice@example.com" },
      { id: "bob", email: "bob@example.com" },
    ];
  }
  return { error: "not-implemented" };
}
