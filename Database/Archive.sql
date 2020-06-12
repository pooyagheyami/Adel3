BEGIN TRANSACTION;
CREATE TABLE `titels` (
	`tit`	TEXT,
	`titel`	TEXT
);
CREATE TABLE "Specify" (
	`Spc`	TEXT,
	`tit`	TEXT,
	`Spcfy`	TEXT
);
CREATE TABLE `Revenu` (
	`date`	TEXT,
	`Rno`	TEXT,
	`Acc`	TEXT,
	`des`	TEXT,
	`Amount`	NUMERIC,
	`Con`	TEXT
);
CREATE TABLE `Respon` (
	`Res`	TEXT,
	`Resname`	TEXT
);
CREATE TABLE "Molks" (
	`Date`	TEXT,
	`Mcode`	TEXT,
	`Res`	TEXT,
	`Mtype`	TEXT,
	`Area`	TEXT,
	`Mname`	TEXT,
	`MSpc`	TEXT,
	`Addrss`	TEXT,
	`M1`	INTEGER,
	`M2`	INTEGER,
	`M3`	INTEGER,
	`M4`	INTEGER,
	`Acc`	TEXT,
	`Amunt1`	NUMERIC,
	`Amunt2`	NUMERIC,
	`des`	TEXT
);
CREATE TABLE `Mntgh` (
	`Area`	TEXT,
	`Aname`	TEXT
);
CREATE TABLE `Mltype` (
	`Mtype`	TEXT,
	`Type`	TEXT
);
CREATE TABLE `MSpcify` (
	`MSpc`	TEXT,
	`Spcfy`	TEXT
);
CREATE TABLE "Descript" (
	`des`	TEXT,
	`dscrpt`	TEXT
);
CREATE TABLE `Account` (
	`Acc`	TEXT,
	`name`	TEXT,
	`phone`	TEXT,
	`Spc`	TEXT,
	`Res`	TEXT
);
COMMIT;
