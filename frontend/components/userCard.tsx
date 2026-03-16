type UserProps = {
  id: string;
  email: string;
  disabled?: boolean;
  masked_email?: string;
};

export function UserCard({ id, email, disabled, masked_email }: UserProps) {
  return (
    <div className="user-card">
      <h3>{id}</h3>
      <p>{masked_email || email}</p>
      {disabled ? <span>Disabled</span> : <span>Active</span>}
    </div>
  );
}
