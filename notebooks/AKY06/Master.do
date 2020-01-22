clear all
set mem 200m
set more off

macro drop _all

global directory "*INSERT PATH TO WORKING FOLDER HERE*"

#delimit ;

foreach dofile in 
SEED.QJEtable.impact.do
SEED.QJEtables.takeup.do
 {;

do "$directory/do files/`dofile'";
};


