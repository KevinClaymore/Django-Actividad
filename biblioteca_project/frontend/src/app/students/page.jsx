"use client";

import { useEffect, useState } from "react";
import { Pagination, PaginationContent, PaginationItem, PaginationNext, PaginationPrevious } from "@/components/ui/pagination";
import CreateStudentDialog from "@/components/CreateStudentDialog";

export default function StudentsPage() {
  const [students, setStudents] = useState([]);
  const [page, setPage] = useState(1);
  const [next, setNext] = useState(null);
  const [previous, setPrevious] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/students/?page=${page}`)
      .then((res) => res.json())
      .then((data) => {
        setStudents(data.results);
        setNext(data.next);
        setPrevious(data.previous);
      });
  }, [page]);

  return (
    <div className="p-6">
      <div className="flex justify-between mb-4">
        <h1 className="text-xl font-bold">Estudiantes</h1>
        <CreateStudentDialog />
      </div>

      <table className="border w-full">
        <thead>
          <tr className="bg-gray-100">
            <th className="border p-2">ID</th>
            <th className="border p-2">Nombre</th>
            <th className="border p-2">Email</th>
            <th className="border p-2">Edad</th>
          </tr>
        </thead>

        <tbody>
          {students.map((s) => (
            <tr key={s.id}>
              <td className="border p-2">{s.id}</td>
              <td className="border p-2">{s.name}</td>
              <td className="border p-2">{s.email}</td>
              <td className="border p-2">{s.age}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* PAGINACIÓN SHADCN */}
      <div className="mt-4">
        <Pagination>
          <PaginationContent>

            <PaginationItem>
              <PaginationPrevious
                className={!previous ? "pointer-events-none opacity-50" : ""}
                onClick={() => previous && setPage(page - 1)}
              />
            </PaginationItem>

            <PaginationItem>
              <PaginationNext
                className={!next ? "pointer-events-none opacity-50" : ""}
                onClick={() => next && setPage(page + 1)}
              />
            </PaginationItem>

          </PaginationContent>
        </Pagination>
      </div>
    </div>
  );
}
