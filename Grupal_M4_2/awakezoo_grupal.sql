--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

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
-- Name: animalitos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.animalitos (
    id bigint NOT NULL,
    nombre character varying(15),
    especie character varying(20)
);


ALTER TABLE public.animalitos OWNER TO postgres;

--
-- Name: animalitos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.animalitos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.animalitos_id_seq OWNER TO postgres;

--
-- Name: animalitos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.animalitos_id_seq OWNED BY public.animalitos.id;


--
-- Name: areas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.areas (
    id bigint NOT NULL,
    " reas" character varying(25),
    supervisor character varying(25),
    encargado_1 character varying(25),
    encargado_2 character varying(25),
    n_especies numeric
);


ALTER TABLE public.areas OWNER TO postgres;

--
-- Name: areas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.areas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.areas_id_seq OWNER TO postgres;

--
-- Name: areas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.areas_id_seq OWNED BY public.areas.id;


--
-- Name: categorias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categorias (
    id bigint NOT NULL,
    categoria character varying(25),
    " rea" character varying(25)
);


ALTER TABLE public.categorias OWNER TO postgres;

--
-- Name: categorias_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categorias_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categorias_id_seq OWNER TO postgres;

--
-- Name: categorias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categorias_id_seq OWNED BY public.categorias.id;


--
-- Name: especies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.especies (
    id bigint NOT NULL,
    especie character varying(25),
    categoria character varying(25)
);


ALTER TABLE public.especies OWNER TO postgres;

--
-- Name: especies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.especies_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.especies_id_seq OWNER TO postgres;

--
-- Name: especies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.especies_id_seq OWNED BY public.especies.id;


--
-- Name: novedades; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.novedades (
    id bigint NOT NULL,
    evento character varying(20),
    hora numeric,
    fecha numeric,
    nota character varying
);


ALTER TABLE public.novedades OWNER TO postgres;

--
-- Name: novedades_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.novedades_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.novedades_id_seq OWNER TO postgres;

--
-- Name: novedades_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.novedades_id_seq OWNED BY public.novedades.id;


--
-- Name: trabajadores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trabajadores (
    id bigint NOT NULL,
    nombre character varying(50),
    rol character varying(25),
    contacto character varying(25),
    sueldo numeric
);


ALTER TABLE public.trabajadores OWNER TO postgres;

--
-- Name: trabajadores_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.trabajadores_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trabajadores_id_seq OWNER TO postgres;

--
-- Name: trabajadores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.trabajadores_id_seq OWNED BY public.trabajadores.id;


--
-- Name: animalitos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animalitos ALTER COLUMN id SET DEFAULT nextval('public.animalitos_id_seq'::regclass);


--
-- Name: areas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.areas ALTER COLUMN id SET DEFAULT nextval('public.areas_id_seq'::regclass);


--
-- Name: categorias id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorias ALTER COLUMN id SET DEFAULT nextval('public.categorias_id_seq'::regclass);


--
-- Name: especies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.especies ALTER COLUMN id SET DEFAULT nextval('public.especies_id_seq'::regclass);


--
-- Name: novedades id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.novedades ALTER COLUMN id SET DEFAULT nextval('public.novedades_id_seq'::regclass);


--
-- Name: trabajadores id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trabajadores ALTER COLUMN id SET DEFAULT nextval('public.trabajadores_id_seq'::regclass);


--
-- Data for Name: animalitos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.animalitos (id, nombre, especie) FROM stdin;
1	Larry	elefante
2	Lennon	chimpance
3	Clau	jirafa
4	L ser	gorila
5	Gaud¡	camello
6	Chiripa	lib‚lula
7	Pati	ara¤a pollito
8	Bee	abeja
9	Manolo	oruga
10	Hulk	escarabajo
11	Pollito	kiwi
12	Freud	picaflor
13	Dandy	c¢ndor
14	Zen	 guila
15	Capone	gaviota
16	Crush	tortugas
17	Lacost	cocodrilo
18	Rango	camaleon
19	Naga	anaconda
20	Basil	pit¢n
21	Apolo	pez globo
22	Denver	salm¢n
23	Bart	pira¤a
24	Capit n	tiburon
25	Pirata	sierra
\.


--
-- Data for Name: areas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.areas (id, " reas", supervisor, encargado_1, encargado_2, n_especies) FROM stdin;
1	mam¡feros y aves	Olga de La Fuente	Rafael Perales	Marco Morillas	10
2	insectos y reptiles	Avelina Alvarado	Manuel Batista	M¢nica Burgos	10
3	peces	Santiago Correa	Andrea Riquelme	Gabriel Sarmiento	5
\.


--
-- Data for Name: categorias; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categorias (id, categoria, " rea") FROM stdin;
1	mam¡feros	mam¡feros y aves
2	aves	mam¡feros y aves
3	insectos	insectos y reptiles
4	reptiles	insectos y reptiles
5	peces	peces
\.


--
-- Data for Name: especies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.especies (id, especie, categoria) FROM stdin;
1	elefante	mam¡fero
2	chimpance	mam¡fero
3	jirafas	mam¡fero
4	gorila	mam¡fero
5	camello	mam¡fero
6	lib‚lula	insectos
7	orugas	insectos
8	abejas	insectos
9	ara¤a	insectos
10	escarabajos	insectos
11	kiwi	aves
12	picaflores	ave
13	condores	ave
14	aguilas	ave
15	gaviota	ave
16	tortuga	reptil
17	cocodrilo	reptil
18	camal‚on	reptil
19	anaconda	reptil
20	pit¢n	reptil
21	pez globo	peces
22	salm¢n	peces
23	pira¤as	peces
24	tibur¢n	peces
25	sierra	peces
\.


--
-- Data for Name: novedades; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.novedades (id, evento, hora, fecha, nota) FROM stdin;
1	inaguraci¢n	\N	\N	\N
2	accidente	\N	\N	\N
3	fuga	\N	\N	\N
4	intrusion	\N	\N	\N
5	enfermedad	\N	\N	\N
6	corte de energ¡a	\N	\N	\N
\.


--
-- Data for Name: trabajadores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.trabajadores (id, nombre, rol, contacto, sueldo) FROM stdin;
1	Olga de La Fuente	supervisor	+56 9 45878460	900000
2	Avelina Alvarado	supervisor	+56 8 75484458	900000
3	Santiago Correa	supervisor	+56 9 55895487	900000
4	Manuel Batista	encargado	+56 9 33258471	600000
5	Marco Morillas	encargado	+56 9 47471258	600000
6	Andrea Riquelme	encargado	+56 9 78884589	600000
7	Rafael Perales	encargado	+56 8 84545112	600000
8	Gabriel Sarmiento	encargado	+56 9 98596632	600000
9	M¢nica Burgos	encargado	+56 5 78745621	600000
\.


--
-- Name: animalitos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.animalitos_id_seq', 25, true);


--
-- Name: areas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.areas_id_seq', 3, true);


--
-- Name: categorias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categorias_id_seq', 5, true);


--
-- Name: especies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.especies_id_seq', 25, true);


--
-- Name: novedades_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.novedades_id_seq', 6, true);


--
-- Name: trabajadores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.trabajadores_id_seq', 9, true);


--
-- PostgreSQL database dump complete
--

