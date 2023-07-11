#ifndef GEO__H
#define GEO__H

#include "stdint.h"
#include <stdio.h>
typedef struct
{
  int8_t  Center_X_i8 ;
  int8_t  Center_Y_i8 ;
  uint8_t Radius_u8   ;
} Cercle_t ;

void Check_Identical ( Cercle_t C1 , Cercle_t C2 ) ;




#endif
