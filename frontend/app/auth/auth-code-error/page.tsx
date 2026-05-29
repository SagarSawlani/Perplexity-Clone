export default function AuthCodeErrorPage() {
  return (
    <div className="min-h-screen bg-background flex items-center justify-center px-4">
      <div className="w-full max-w-md text-center">
        <div className="bg-card border border-border rounded-lg p-10 shadow-sm">
          <div className="text-5xl mb-6">⚠️</div>
          <h1 className="text-2xl font-bold text-foreground mb-3">
            Authentication Error
          </h1>
          <p className="text-muted-foreground mb-8">
            Something went wrong during sign-in. The link may have expired or
            already been used. Please try again.
          </p>
          <a
            href="/"
            className="inline-flex items-center justify-center h-11 px-6 rounded-lg bg-foreground text-background font-medium text-sm hover:bg-foreground/90 transition-colors"
          >
            Back to Sign In
          </a>
        </div>
      </div>
    </div>
  );
}
