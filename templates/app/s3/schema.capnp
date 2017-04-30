
@0xae0e1b3230acbd1c;
struct Schema {
	image @0 :Text = "Ubuntu 16.04 x64";
	vdc @1 :Text;
	sshkey @2 :Text;
	disk @3 :List(Text);
	hostprefix @4 :Text;
	fqdn @5 :Text;
	keyAccess @6 :Text;
	keySecret @7 :Text;
	enablehttps @8 :Bool = false;

}
