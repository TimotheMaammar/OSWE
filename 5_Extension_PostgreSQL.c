
#include "postgres.h"
#include <string.h>
#include "fmgr.h"
#include "utils/geo_decls.h"
#include <stdio.h>
#include "utils/builtins.h"

#ifdef PG_MODULE_MAGIC
PG_MODULE_MAGIC;
#endif

/* Add a prototype marked PGDLLEXPORT */
PGDLLEXPORT Datum awae(PG_FUNCTION_ARGS);
PG_FUNCTION_INFO_V1(awae);

/* this function launches the executable passed in as the first parameter
   in a FOR loop bound by the second parameter that is also passed*/
Datum
awae(PG_FUNCTION_ARGS)
{
    /* convert text pointer to C string */
    #define GET_STR(textp) DatumGetCString(DirectFunctionCall1(textout, PointerGetDatum(textp)))

    /* retrieve the second argument that is passed to the function (an integer)
       that will serve as our counter limit*/
    int instances = PG_GETARG_INT32(1);

    for (int c = 0; c < instances; c++) {
        /* launch the process passed in the first parameter */
        ShellExecute(NULL, "open", GET_STR(PG_GETARG_TEXT_P(0)), NULL, NULL, 1);
    }

    PG_RETURN_VOID();
}
