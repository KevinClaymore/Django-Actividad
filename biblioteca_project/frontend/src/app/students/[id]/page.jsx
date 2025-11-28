"use client";

import { useEffect, useState } from "react";

export default function StudentDetail({ params }) {
  const { id } = params;
  const [student, setStudent] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/students/${id}/`)
      .then(res => res.json())
      .then(setStudent);
  }, []);

  if (!student) return <p className="p-6">Cargando...</p>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Detalle del estudiante</h1>

      <p><strong>ID:</strong> {student.id}</p>
      <p><strong>Nombre:</strong> {student.name}</p>
      <p><strong>Email:</strong> {student.email}</p>
      <p><strong>Edad:</strong> {student.age}</p>
    </div>
  );
}
