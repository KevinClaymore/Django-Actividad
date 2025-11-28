"use client";

import { useState } from "react";
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog";

export default function CreateStudentDialog() {
  const [open, setOpen] = useState(false);
  const [form, setForm] = useState({
    name: "",
    email: "",
    age: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch("http://127.0.0.1:8000/api/students/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form),
    });

    if (res.ok) {
      setOpen(false);        // cerrar modal
      setForm({              // limpiar formulario
        name: "",
        email: "",
        age: "",
      });
      window.location.reload(); // refrescar lista
    }
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger className="px-3 py-2 bg-blue-500 text-white rounded">
        Crear estudiante
      </DialogTrigger>

      <DialogContent className="p-6">
        <h2 className="font-bold mb-4">Crear estudiante</h2>

        <form onSubmit={handleSubmit} className="space-y-3">
          <input
            name="name"
            placeholder="Nombre"
            className="w-full border p-2"
            value={form.name}
            onChange={handleChange}
          />

          <input
            name="email"
            placeholder="Email"
            className="w-full border p-2"
            value={form.email}
            onChange={handleChange}
          />

          <input
            name="age"
            placeholder="Edad"
            type="number"
            className="w-full border p-2"
            value={form.age}
            onChange={handleChange}
          />

          <button className="w-full bg-green-500 text-white py-2 rounded">
            Guardar
          </button>
        </form>
      </DialogContent>
    </Dialog>
  );
}
