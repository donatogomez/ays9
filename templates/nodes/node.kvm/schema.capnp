
@0x8e6e6642ebc07636;
struct Schema {
	os @0 :Text;
	image @1 :Text;
	disks @2 :List(Int64);
	nics @3 :List(Text);
	memory @4 :Int64 = 256;
	cpu @5 :Int64 = 1;
	ipPublic @6 :Text;
	ipPrivate @7 :Text;
	sshLogin @8 :Text = "root";
	sshPassword @9 :Text = "gig1234";

}
