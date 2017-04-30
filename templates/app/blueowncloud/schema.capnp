
@0xa5f47e75c1d8fea1;
struct Schema {
	vdc @0 :Text;
	sshkey @1 :Text;
	datadisks @2 :List(Int64);
	hostprefix @3 :Text;
	fqdn @4 :Text;
	enablehttps @5 :Bool = false;

}
