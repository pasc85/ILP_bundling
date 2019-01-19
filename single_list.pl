#!/usr/bin/perl -w

$on1=0;
$on2=0;
while (<>) {
  if ($on1) {
    s!\s*<td>!!;
    s!</td>\s*!!;
    @F=split;
    $surname=pop(@F);
    $forename=pop(@F);
    print "$surname, $forename, ";
    $on1=0;
  };
  if ($on2) {
    s!\s*<td>!!;
    s!</td>\s*!!;
    @F=split;
    $id=pop(@F);
    print "$id\n";
    $on2=0;
  };
  /Name/ and $on1=1;
  /Student\sID/ and $on2=1;
}
