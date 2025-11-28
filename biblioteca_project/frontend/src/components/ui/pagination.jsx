"use client";

import React from "react";
import { cn } from "@/lib/utils";

export function Pagination({ className, ...props }) {
  return (
    <nav
      role="navigation"
      aria-label="pagination"
      className={cn("mx-auto flex w-full justify-center", className)}
      {...props}
    />
  );
}

export function PaginationContent({ className, ...props }) {
  return (
    <ul
      className={cn("flex flex-row items-center gap-1", className)}
      {...props}
    />
  );
}

export function PaginationItem({ className, ...props }) {
  return <li className={cn("", className)} {...props} />;
}

export function PaginationPrevious({ className, ...props }) {
  return (
    <button
      className={cn(
        "flex h-9 items-center justify-center rounded-md border px-4 py-2 text-sm hover:bg-muted",
        className
      )}
      {...props}
    >
      Anterior
    </button>
  );
}

export function PaginationNext({ className, ...props }) {
  return (
    <button
      className={cn(
        "flex h-9 items-center justify-center rounded-md border px-4 py-2 text-sm hover:bg-muted",
        className
      )}
      {...props}
    >
      Siguiente
    </button>
  );
}
