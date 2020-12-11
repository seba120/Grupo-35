--
-- PostgreSQL database dump
--

-- Dumped from database version 11.10
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

--
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    id_cliente bigint NOT NULL,
    nombre_cliente character varying(50) NOT NULL,
    apellido_cliente character varying(50) NOT NULL,
    telefono_cliente numeric NOT NULL,
    mail_cliente character varying(100),
    dia_pago_suscripcion numeric NOT NULL
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- Name: cliente_id_cliente_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cliente_id_cliente_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cliente_id_cliente_seq OWNER TO postgres;

--
-- Name: cliente_id_cliente_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cliente_id_cliente_seq OWNED BY public.cliente.id_cliente;


--
-- Name: cliente_pase; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente_pase (
    id_cliente integer NOT NULL,
    id_pase integer NOT NULL
);


ALTER TABLE public.cliente_pase OWNER TO postgres;

--
-- Name: cliente_suscripcion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente_suscripcion (
    id_cliente integer NOT NULL,
    id_suscripcion integer NOT NULL
);


ALTER TABLE public.cliente_suscripcion OWNER TO postgres;

--
-- Name: pase; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pase (
    id_pase bigint NOT NULL,
    nombre_pase character varying(50) NOT NULL,
    detalle_pase character varying(100) NOT NULL,
    valor_pase integer NOT NULL
);


ALTER TABLE public.pase OWNER TO postgres;

--
-- Name: pase_id_pase_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pase_id_pase_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pase_id_pase_seq OWNER TO postgres;

--
-- Name: pase_id_pase_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pase_id_pase_seq OWNED BY public.pase.id_pase;


--
-- Name: producto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producto (
    id_producto bigint NOT NULL,
    nombre_producto character varying(50) NOT NULL,
    detalle_producto character varying(50) NOT NULL,
    precio_producto numeric NOT NULL,
    stock_producto numeric NOT NULL
);


ALTER TABLE public.producto OWNER TO postgres;

--
-- Name: producto_id_producto_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.producto_id_producto_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producto_id_producto_seq OWNER TO postgres;

--
-- Name: producto_id_producto_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.producto_id_producto_seq OWNED BY public.producto.id_producto;


--
-- Name: suscripcion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.suscripcion (
    id_suscripcion bigint NOT NULL,
    nombre_suscripcion character varying(50) NOT NULL,
    detalle_suscripcion character varying(300) NOT NULL,
    precio_suscripcion integer NOT NULL
);


ALTER TABLE public.suscripcion OWNER TO postgres;

--
-- Name: suscripcion_id_suscripcion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.suscripcion_id_suscripcion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.suscripcion_id_suscripcion_seq OWNER TO postgres;

--
-- Name: suscripcion_id_suscripcion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.suscripcion_id_suscripcion_seq OWNED BY public.suscripcion.id_suscripcion;


--
-- Name: transaccion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transaccion (
    id_transaccion bigint NOT NULL,
    fecha_transaccion date DEFAULT CURRENT_DATE,
    id_cliente integer NOT NULL
);


ALTER TABLE public.transaccion OWNER TO postgres;

--
-- Name: transaccion_id_transaccion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.transaccion_id_transaccion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.transaccion_id_transaccion_seq OWNER TO postgres;

--
-- Name: transaccion_id_transaccion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.transaccion_id_transaccion_seq OWNED BY public.transaccion.id_transaccion;


--
-- Name: transaccion_pase; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transaccion_pase (
    id_transaccion integer NOT NULL,
    id_pase integer NOT NULL,
    fecha_pase date DEFAULT CURRENT_DATE
);


ALTER TABLE public.transaccion_pase OWNER TO postgres;

--
-- Name: transaccion_producto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transaccion_producto (
    id_transaccion integer NOT NULL,
    id_producto integer NOT NULL,
    cantidad_producto integer NOT NULL
);


ALTER TABLE public.transaccion_producto OWNER TO postgres;

--
-- Name: transaccion_suscripcion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transaccion_suscripcion (
    id_transaccion integer NOT NULL,
    id_suscripcion integer NOT NULL
);


ALTER TABLE public.transaccion_suscripcion OWNER TO postgres;

--
-- Name: cliente id_cliente; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente ALTER COLUMN id_cliente SET DEFAULT nextval('public.cliente_id_cliente_seq'::regclass);


--
-- Name: pase id_pase; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pase ALTER COLUMN id_pase SET DEFAULT nextval('public.pase_id_pase_seq'::regclass);


--
-- Name: producto id_producto; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto ALTER COLUMN id_producto SET DEFAULT nextval('public.producto_id_producto_seq'::regclass);


--
-- Name: suscripcion id_suscripcion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.suscripcion ALTER COLUMN id_suscripcion SET DEFAULT nextval('public.suscripcion_id_suscripcion_seq'::regclass);


--
-- Name: transaccion id_transaccion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaccion ALTER COLUMN id_transaccion SET DEFAULT nextval('public.transaccion_id_transaccion_seq'::regclass);


--
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cliente (id_cliente, nombre_cliente, apellido_cliente, telefono_cliente, mail_cliente, dia_pago_suscripcion) FROM stdin;
1	Sebastían	Boettiger	55555555	seba@seba.com	5
2	Katherine	Barrera	77777777	k@k.com	10
3	Jaime	Lepin	44444444	jaime@jaime.com	15
4	Alfonso	Madrid	66666666	alf@alf.com	1
5	Lalo	Landas	12345678	lalo@l.com	10
6	Beto A.	Saber	99999999	bt@saber.com	1
7	Ash	Ketchup	11111111	a.k@pueblopaleta.com	5
8	Nikola	Tesla	22222222	niko@tesla.com	10
9	Guido	Van Rossum	33333333	gvr@python.net	15
10	James	Gosling	88888888	nosirvo@java.com	20
11	Brendan	Eich	99998888	whatever@js.io	25
12	Isaac	Schlueter	88887777	isaac@npm.com	30
13	Linus	Torvalds	77776666	lt@git.io	1
14	Niklaus	Wirth	66665555	viejo@pascale.com	5
15	Tim	Berners-Lee	55554444	timy@web.com	10
16	Michael	Stonebraker	44443333	mstone@psql.net	15
17	Jonathan	Olave	33332222	jonaawaker@awakelab.cl	20
18	Luis	Jaraquemada	22221111	luchitoawaker@awakelab.cl	25
19	Armando	Casas	11110000	ac@ac.com	30
20	Aquiles	Basaez	90909090	ab@ab.com	1
\.


--
-- Data for Name: cliente_pase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cliente_pase (id_cliente, id_pase) FROM stdin;
\.


--
-- Data for Name: cliente_suscripcion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cliente_suscripcion (id_cliente, id_suscripcion) FROM stdin;
1	5
2	4
3	2
4	3
5	1
6	5
7	4
8	3
9	2
10	1
11	1
12	2
13	3
14	4
15	5
16	5
17	4
18	3
19	2
20	1
\.


--
-- Data for Name: pase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pase (id_pase, nombre_pase, detalle_pase, valor_pase) FROM stdin;
1	matutino	valido de 07:00 a 11:59	2000
2	break office	valido de 12:00 a 16:59	2400
3	after office	valido desde 17:00 a 19:59	2400
4	vespertino	valido desde 20:00 a 23:59	3000
5	nocturno	valido desde 00:00 a 03:00	1500
\.


--
-- Data for Name: producto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producto (id_producto, nombre_producto, detalle_producto, precio_producto, stock_producto) FROM stdin;
1	agua mineral	Cachantun 500cc	700	350
2	agua mineral	Benedictino 1l	1400	350
3	isotónica	powerade 1 l	2000	500
4	barra energética	squeezy 50g	1000	1000
5	energética	monster 0 azúcar	2500	1000
6	energética	red bull	2200	800
7	toalla personal	tamaño 40x60	4000	200
8	banda elastica	par grado 4	10000	100
9	mancuernas	par 1kg	8000	80
10	mancuernas	par 5kg	25000	40
11	callera	anti-ripper everlast	18000	50
12	magnesio gimnasia	calistenia 250gr	4000	100
13	foam roller	masajeador corporal	16000	40
14	tatami	suelo deportivo	23000	200
15	morral deportivo	10 litros	5000	100
\.


--
-- Data for Name: suscripcion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.suscripcion (id_suscripcion, nombre_suscripcion, detalle_suscripcion, precio_suscripcion) FROM stdin;
1	Mensual	Cliente puede participar de todas las clases e instalaciones del gymAsia durante 30 días desde la contratación.	30000
2	Trimestral	Cliente puede participar de todas las clases e instalaciones del gymAsia durante 90 días desde la contratación.	90000
3	Semestral	Cliente puede participar de todas las clases e instalaciones del gymAsia durante 120 días desde la contratación.	120000
4	Anual	Cliente puede participar de todas las clases e instalaciones del gymAsia durante 1 año desde la contratación.	150000
5	Estudiante	Plan especial para estudiantes desde los 16 años, donde el cliente puede participar de todas las clases e instalaciones del gymAsia durante 30 días hasta las 16:00 hrs.	20000
\.


--
-- Data for Name: transaccion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transaccion (id_transaccion, fecha_transaccion, id_cliente) FROM stdin;
\.


--
-- Data for Name: transaccion_pase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transaccion_pase (id_transaccion, id_pase, fecha_pase) FROM stdin;
\.


--
-- Data for Name: transaccion_producto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transaccion_producto (id_transaccion, id_producto, cantidad_producto) FROM stdin;
\.


--
-- Data for Name: transaccion_suscripcion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transaccion_suscripcion (id_transaccion, id_suscripcion) FROM stdin;
\.


--
-- Name: cliente_id_cliente_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cliente_id_cliente_seq', 20, true);


--
-- Name: pase_id_pase_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pase_id_pase_seq', 5, true);


--
-- Name: producto_id_producto_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.producto_id_producto_seq', 15, true);


--
-- Name: suscripcion_id_suscripcion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.suscripcion_id_suscripcion_seq', 5, true);


--
-- Name: transaccion_id_transaccion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transaccion_id_transaccion_seq', 1, false);


--
-- Name: cliente_pase cliente_pase_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente_pase
    ADD CONSTRAINT cliente_pase_pkey PRIMARY KEY (id_cliente, id_pase);


--
-- Name: cliente cliente_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pk PRIMARY KEY (id_cliente);


--
-- Name: cliente_suscripcion cliente_suscripcion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente_suscripcion
    ADD CONSTRAINT cliente_suscripcion_pkey PRIMARY KEY (id_cliente, id_suscripcion);


--
-- Name: pase pase_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pase
    ADD CONSTRAINT pase_pk PRIMARY KEY (id_pase);


--
-- Name: producto producto_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto
    ADD CONSTRAINT producto_pk PRIMARY KEY (id_producto);


--
-- Name: suscripcion suscripcion_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.suscripcion
    ADD CONSTRAINT suscripcion_pk PRIMARY KEY (id_suscripcion);


--
-- Name: transaccion_pase transaccion_pase_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaccion_pase
    ADD CONSTRAINT transaccion_pase_pkey PRIMARY KEY (id_transaccion, id_pase);


--
-- Name: transaccion transaccion_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaccion
    ADD CONSTRAINT transaccion_pk PRIMARY KEY (id_transaccion);


--
-- Name: transaccion_producto transaccion_producto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaccion_producto
    ADD CONSTRAINT transaccion_producto_pkey PRIMARY KEY (id_transaccion, id_producto);


--
-- Name: transaccion_suscripcion transaccion_suscripcion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaccion_suscripcion
    ADD CONSTRAINT transaccion_suscripcion_pkey PRIMARY KEY (id_transaccion, id_suscripcion);


--
-- Name: transaccion cli_tran_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaccion
    ADD CONSTRAINT cli_tran_fk FOREIGN KEY (id_cliente) REFERENCES public.cliente(id_cliente) ON DELETE SET NULL;


--
-- PostgreSQL database dump complete
--

