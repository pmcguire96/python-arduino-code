// player object
// component > physics > rigid body

// create > material > change color to make it suck less
// no rotation? contraint settings

// 1. Just make an object move around
// 2. Tell if player is touching a coin it needs to collect
//    		

using UnityEngine;
using System.Collections;

public class Player : MonoBehavior {
	
	public float speed = 6;
	int coinCount;
	Vector3 velocity;
	
	Rigidbody myRigidbody;
	
	void Start () {
		myRigidbody = GetComponent<Rigidbody> (); // getComponent is a generic method. Syntax: <TYPE>
		
	}
	
	void Update () {
		Vector3 input = new Vector3(Input.GetAxisRaw ("Horizontal"), 0, Input.GetAxisRaw("Vertical"));
		Vector3 direction = Input.normalized; 
		Vector3 velocity = direction * speed;
		
	}
	
	void FixedUpdate () { // track objects during frame drops, prevent passing through walls if collision is skipped
		myRigidbody.position += velocity * Time.fixedDeltaTime; // Time.deltaTime works too
	}
	
	void OnTriggerEnter(Collider triggerCollider){ // one collider must be a trigger, one must have rigid body (both can be on one)
		//print(triggerCollider.gameObject.name); // isKinematic checkbox removes physics
		// add tags in Inspector
		if (triggerCollider.tag == "Coin") {
			Destroy(triggerCollider.gameObject);
			coinCount++;
			print("Number of coins: " + coinCount);
		}
	}
}