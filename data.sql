--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0
-- Dumped by pg_dump version 12.0

-- Started on 2019-10-10 01:45:56

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 16402)
-- Name: Job; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Job" (
    id integer NOT NULL,
    name text
);


ALTER TABLE public."Job" OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16394)
-- Name: Machine; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Machine" (
    id integer NOT NULL,
    name text,
    enabled boolean,
    type text
);


ALTER TABLE public."Machine" OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16410)
-- Name: Task; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Task" (
    id integer NOT NULL,
    name text,
    job_id integer,
    sequence integer
);


ALTER TABLE public."Task" OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16423)
-- Name: Task_queue; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Task_queue" (
    id integer NOT NULL,
    machine_id integer,
    task_id integer,
    status text
);


ALTER TABLE public."Task_queue" OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16441)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 2842 (class 0 OID 16402)
-- Dependencies: 203
-- Data for Name: Job; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Job" (id, name) VALUES (1, 'Develop');
INSERT INTO public."Job" (id, name) VALUES (2, 'Design');


--
-- TOC entry 2841 (class 0 OID 16394)
-- Dependencies: 202
-- Data for Name: Machine; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Machine" (id, name, enabled, type) VALUES (1, 'Bee', true, 'Task A');


--
-- TOC entry 2843 (class 0 OID 16410)
-- Dependencies: 204
-- Data for Name: Task; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Task" (id, name, job_id, sequence) VALUES (1, 'Task A', 1, 1);


--
-- TOC entry 2844 (class 0 OID 16423)
-- Dependencies: 205
-- Data for Name: Task_queue; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Task_queue" (id, machine_id, task_id, status) VALUES (1, 1, 1, 'Complete');


--
-- TOC entry 2845 (class 0 OID 16441)
-- Dependencies: 206
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alembic_version (version_num) VALUES ('c30a3aec3b6a');


--
-- TOC entry 2708 (class 2606 OID 16409)
-- Name: Job Job_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Job"
    ADD CONSTRAINT "Job_pkey" PRIMARY KEY (id);


--
-- TOC entry 2706 (class 2606 OID 16401)
-- Name: Machine Machine_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Machine"
    ADD CONSTRAINT "Machine_pkey" PRIMARY KEY (id);


--
-- TOC entry 2710 (class 2606 OID 16417)
-- Name: Task Task_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Task"
    ADD CONSTRAINT "Task_pkey" PRIMARY KEY (id);


--
-- TOC entry 2712 (class 2606 OID 16430)
-- Name: Task_queue Task_queue_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Task_queue"
    ADD CONSTRAINT "Task_queue_pkey" PRIMARY KEY (id);


--
-- TOC entry 2714 (class 2606 OID 16445)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


-- Completed on 2019-10-10 01:46:04

--
-- PostgreSQL database dump complete
--

